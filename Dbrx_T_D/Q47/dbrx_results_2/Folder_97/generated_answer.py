def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[28:95].lower()
    lengths = range(38, 50)
    for length in lengths:
        for i in range(len(substring) - length + 1):
            if substring[i:i + length] == substring[i:i + length][::-1]:
                result.add(substring[i:i + length])
    return result