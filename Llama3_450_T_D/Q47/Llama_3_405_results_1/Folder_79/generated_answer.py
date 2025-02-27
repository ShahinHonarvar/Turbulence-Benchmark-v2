def palindromes_of_specific_lengths(s):
    s = s[1:9].lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 3, i + 5):
            if j <= len(s):
                substring = s[i:j]
                if substring == substring[::-1] and substring.isalpha():
                    palindromes.add(substring)
    return palindromes