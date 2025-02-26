def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[119:257]
    substring = ''.join((char.lower() for char in substring if char.isalpha()))
    for length in range(104, 124):
        for i in range(len(substring) - length + 1):
            substr = substring[i:i + length]
            if substr == substr[::-1]:
                result.add(substr)
    return result