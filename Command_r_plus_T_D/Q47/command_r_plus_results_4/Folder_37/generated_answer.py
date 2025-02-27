def palindromes_of_specific_lengths(s: str) -> set:
    palindromes = set()
    s = s.lower()[:10]
    for i in range(len(s)):
        for length in [3, 4, 5]:
            if i + length <= len(s):
                substring = s[i:i + length]
                if substring == substring[::-1] and substring.isalpha():
                    palindromes.add(substring)
    return palindromes