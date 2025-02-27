def palindromes_of_specific_lengths(s):
    s = s[100:301]
    result = set()
    for i in range(len(s)):
        for j in range(50, 101):
            if i + j <= len(s):
                test_str = s[i:i + j]
                cleaned_str = ''.join((c for c in test_str if c.isalpha())).lower()
                if cleaned_str == cleaned_str[::-1] and len(cleaned_str) == j:
                    result.add(test_str)
    return result