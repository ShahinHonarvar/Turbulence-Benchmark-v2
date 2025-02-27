def palindromes_of_specific_lengths(s):
    s = s[32:80]
    palindromes = set()
    for start in range(len(s)):
        for length in range(35, 42):
            if start + length <= len(s):
                substr = s[start:start + length]
                cleaned = ''.join(filter(str.isalpha, substr)).lower()
                if cleaned == cleaned[::-1] and 35 <= len(cleaned) <= 41:
                    palindromes.add(cleaned)
    return palindromes