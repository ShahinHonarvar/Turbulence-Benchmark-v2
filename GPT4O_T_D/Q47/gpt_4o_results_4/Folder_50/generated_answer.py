def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[36:93]
    substring = ''.join(filter(str.isalpha, substring)).lower()
    n = len(substring)
    for start in range(n):
        for length in range(10, 36):
            if start + length <= n:
                candidate = substring[start:start + length]
                if candidate == candidate[::-1]:
                    result.add(candidate)
    return result