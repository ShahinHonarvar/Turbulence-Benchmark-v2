def palindromes_of_specific_lengths(s):
    s = s[1:8]
    s = ''.join(filter(str.isalpha, s)).lower()
    palindromes = set()
    for i in range(len(s)):
        for length in range(3, 5):
            if i + length <= len(s):
                substring = s[i:i + length]
                if substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes