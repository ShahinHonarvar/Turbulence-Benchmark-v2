def palindromes_between_indices(s):
    sub_str = s[3:7].lower()
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    palindromes = set()
    for i in range(len(sub_str)):
        for j in range(i + 3, len(sub_str) + 1):
            window = sub_str[i:j]
            if window == window[::-1] and all((char in english_letters for char in window)):
                palindromes.add(window)
    return palindromes