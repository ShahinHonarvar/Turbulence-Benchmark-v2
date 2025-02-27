def palindromes_of_specific_lengths(s):
    s = s[11:84].lower()
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    palindromes = set()
    for length in range(37, 61):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if set(substring) <= alphabet and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes