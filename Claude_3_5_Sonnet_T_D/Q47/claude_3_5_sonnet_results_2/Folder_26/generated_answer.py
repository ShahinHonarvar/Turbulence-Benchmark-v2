def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[24:85]
    substring = ''.join((c.lower() for c in substring if c.isalpha()))
    for i in range(len(substring)):
        for j in range(i + 21, min(i + 32, len(substring) + 1)):
            if j - i > 31:
                break
            candidate = substring[i:j]
            if candidate == candidate[::-1]:
                result.add(candidate)
    return result