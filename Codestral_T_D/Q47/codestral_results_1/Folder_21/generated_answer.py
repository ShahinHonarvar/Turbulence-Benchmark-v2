def palindromes_of_specific_lengths(s):
    s = s[100:296].lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 136, min(i + 161, len(s))):
            substring = s[i:j + 1]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes