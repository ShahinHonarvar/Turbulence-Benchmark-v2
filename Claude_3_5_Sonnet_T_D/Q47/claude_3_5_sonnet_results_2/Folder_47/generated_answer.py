def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[39:95]
    substring = ''.join((c.lower() for c in substring if c.isalpha()))
    for i in range(len(substring)):
        for j in range(i + 14, min(i + 53, len(substring) + 1)):
            if j - i > 52:
                break
            substr = substring[i:j]
            if substr == substr[::-1]:
                result.add(substr)
    return result