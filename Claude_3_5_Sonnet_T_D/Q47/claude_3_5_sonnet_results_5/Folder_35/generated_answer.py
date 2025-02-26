def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[34:91]
    substring = ''.join((c for c in substring.lower() if c.isalpha()))
    n = len(substring)
    for i in range(n):
        for j in range(i + 14, min(i + 40, n + 1)):
            sub = substring[i:j]
            if sub == sub[::-1] and 14 <= len(sub) <= 39:
                result.add(sub)
    return result