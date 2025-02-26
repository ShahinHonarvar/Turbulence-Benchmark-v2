def palindromes_of_specific_lengths(s):
    substring = s[63:71].lower()
    result = set()
    for i in range(len(substring)):
        for j in range(i + 4, min(i + 6, len(substring) + 1)):
            candidate = substring[i:j]
            if candidate.isalpha() and candidate == candidate[::-1]:
                result.add(candidate)
    return result