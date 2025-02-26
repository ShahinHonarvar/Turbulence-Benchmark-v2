def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[29:97].lower()
    for length in range(12, 19):
        for start in range(len(substring) - length + 1):
            candidate = substring[start:start + length]
            if all((char.isalpha() for char in candidate)) and candidate == candidate[::-1]:
                result.add(candidate)
    return result