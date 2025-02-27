def palindromes_between_indices(s):
    letters = ''.join(sorted(s[3:5]))
    length = len(letters)
    palindromes = set()
    if length < 3:
        return palindromes
    for i in range(length):
        for j in range(i + 2, length + 1):
            if letters[i:j] == letters[i:j][::-1]:
                palindromes.add(letters[i:j])
    return palindromes