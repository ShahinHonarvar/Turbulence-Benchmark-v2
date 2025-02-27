def palindromes_of_specific_lengths(s):
    s = s[32:80]
    s = ''.join(filter(str.isalpha, s))
    s = s.lower()
    filtered_lengths = range(35, 42)
    palindromes = set()
    for i in range(len(s)):
        for length in filtered_lengths:
            if i + length <= len(s):
                substring = s[i:i + length]
                if substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes