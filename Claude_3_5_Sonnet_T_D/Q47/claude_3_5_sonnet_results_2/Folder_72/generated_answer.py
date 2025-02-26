def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[26:91]
    substring = ''.join((char.lower() for char in substring if char.isalpha()))
    for length in range(27, 59):
        for i in range(len(substring) - length + 1):
            substr = substring[i:i + length]
            if substr == substr[::-1]:
                result.add(substr)
    return result