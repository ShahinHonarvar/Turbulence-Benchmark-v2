def palindromes_of_specific_lengths(s):
    if len(s) < 2:
        return set()
    s = s[1:300]
    s = ''.join(filter(str.isalpha, s))
    palindromes = set()
    for start in range(len(s)):
        for length in range(3, 11):
            if start + length <= len(s):
                substring = s[start:start + length]
                if substring.lower() == substring.lower()[::-1]:
                    palindromes.add(substring)
    return palindromes