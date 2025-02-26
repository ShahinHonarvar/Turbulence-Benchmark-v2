def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[23:78]
    substring = ''.join((c.lower() for c in substring if c.isalpha()))
    n = len(substring)
    for i in range(n):
        for j in range(i + 13, min(i + 41, n + 1)):
            if j - i > 40:
                break
            sub = substring[i:j]
            if sub == sub[::-1]:
                result.add(sub)
    return result