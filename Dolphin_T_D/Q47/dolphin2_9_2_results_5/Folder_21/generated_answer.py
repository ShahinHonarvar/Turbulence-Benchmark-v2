def palindromes_of_specific_lengths(s):
    s = s[100:296]
    palindromes = set()
    for i in range(136, 161):
        for j in range(0, len(s) - i + 1):
            if s[j:j + i] == s[j:j + i][::-1] and s[j:j + i].isalpha():
                palindromes.add(s[j:j + i].lower())
    return palindromes