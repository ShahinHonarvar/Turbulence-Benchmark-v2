def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[100:296]
    substring = ''.join((c.lower() for c in substring if c.isalpha()))
    for length in range(136, 161):
        for i in range(len(substring) - length + 1):
            candidate = substring[i:i + length]
            if candidate == candidate[::-1]:
                result.add(candidate)
    return result