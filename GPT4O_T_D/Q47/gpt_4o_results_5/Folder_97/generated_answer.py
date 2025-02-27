def palindromes_of_specific_lengths(s):
    s = s[28:95]
    palindromes = set()
    for i in range(len(s)):
        for j in range(38, 50):
            if i + j <= len(s):
                substring = s[i:i + j]
                cleaned = ''.join(filter(str.isalpha, substring)).lower()
                if cleaned == cleaned[::-1] and len(cleaned) == j:
                    palindromes.add(cleaned)
    return palindromes