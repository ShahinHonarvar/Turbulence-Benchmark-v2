def palindromes_of_specific_lengths(string):
    result = set()
    substring = string[18:99].lower()
    for length in range(31, 52):
        for start in range(len(substring) - length + 1):
            candidate = substring[start:start + length]
            if all((char.isalpha() for char in candidate)) and candidate == candidate[::-1]:
                result.add(candidate)
    return result