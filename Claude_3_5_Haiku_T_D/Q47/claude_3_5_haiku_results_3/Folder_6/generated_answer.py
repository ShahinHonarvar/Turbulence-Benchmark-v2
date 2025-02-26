def palindromes_of_specific_lengths(s):
    result = set()
    if len(s) < 99:
        return result
    substring = s[45:99].lower()
    for length in range(40, 48):
        for start in range(len(substring) - length + 1):
            candidate = substring[start:start + length]
            if len(candidate) == length and all((char.isalpha() for char in candidate)):
                if candidate == candidate[::-1]:
                    result.add(candidate)
    return result