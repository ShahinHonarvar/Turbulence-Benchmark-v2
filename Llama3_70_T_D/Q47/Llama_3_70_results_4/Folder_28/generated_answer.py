def palindromes_of_specific_lengths(s):
    s = s[32:72].lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 21, min(len(s) + 1, i + 33)):
            substring = s[i:j]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes