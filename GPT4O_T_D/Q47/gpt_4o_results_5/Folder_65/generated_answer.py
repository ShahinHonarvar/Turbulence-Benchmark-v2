def palindromes_of_specific_lengths(s):
    result = set()
    substring = ''.join((c for c in s[15:96] if c.isalpha()))
    for length in range(20, 67):
        for i in range(len(substring) - length + 1):
            candidate = substring[i:i + length]
            if candidate.lower() == candidate[::-1].lower():
                result.add(candidate)
    return result