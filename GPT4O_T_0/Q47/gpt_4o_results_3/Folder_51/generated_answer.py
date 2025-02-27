def palindromes_of_specific_lengths(s):
    s = s[2:9]
    s = ''.join(filter(str.isalpha, s)).lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(3, 5):
            if i + j <= len(s):
                substring = s[i:i + j]
                if substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes