def palindromes_of_specific_lengths(s):
    s = s[26:85].lower()
    palindromes = set()
    for i in range(30, 47):
        for j in range(len(s) - i + 1):
            if s[j:j + i] == s[j:j + i][::-1] and s[j:j + i].isalpha():
                palindromes.add(s[j:j + i])
    return palindromes