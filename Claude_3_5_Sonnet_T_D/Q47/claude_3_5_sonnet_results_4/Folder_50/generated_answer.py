def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[36:93]
    cleaned = ''.join((char.lower() for char in substring if char.isalpha()))
    for length in range(10, 36):
        for i in range(len(cleaned) - length + 1):
            potential = cleaned[i:i + length]
            if potential == potential[::-1]:
                result.add(potential)
    return result