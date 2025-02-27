def palindromes_between_indices(s):
    letters = sorted([ch for ch in s[3:10] if ch in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'])
    length = len(letters)
    if length < 5:
        return set()
    palindromes = set()
    for i in range(0, length):
        for j in range(i, length):
            if letters[i] == letters[j] and length - i - j >= 2:
                center = ''
                for k in range(i, j + 1):
                    center += letters[k]
                for k in range(j + 1, i - 1, -1):
                    palindromes.add(center + letters[k].lower() + center)
    return palindromes