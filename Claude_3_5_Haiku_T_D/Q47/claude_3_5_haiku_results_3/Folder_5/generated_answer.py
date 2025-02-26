def palindromes_of_specific_lengths(s):
    if len(s) < 71:
        return set()
    substring = s[63:71].lower()
    result = set()
    for start in range(len(substring)):
        for length in range(4, 6):
            if start + length > len(substring):
                break
            candidate = substring[start:start + length]
            if all((char.isalpha() for char in candidate)) and candidate == candidate[::-1]:
                result.add(candidate)
    return result