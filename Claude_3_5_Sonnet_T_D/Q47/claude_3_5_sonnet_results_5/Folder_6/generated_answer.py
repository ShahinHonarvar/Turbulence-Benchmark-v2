def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[45:99]
    cleaned = ''.join((c.lower() for c in substring if c.isalpha()))
    for length in range(40, 48):
        for i in range(len(cleaned) - length + 1):
            potential = cleaned[i:i + length]
            if potential == potential[::-1]:
                result.add(potential)
    return result