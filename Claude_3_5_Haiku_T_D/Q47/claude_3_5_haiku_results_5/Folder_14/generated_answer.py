def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[10:75]
    for length in range(6, 9):
        for i in range(len(substring) - length + 1):
            candidate = substring[i:i + length]
            if candidate.isalpha() and candidate.lower() == candidate.lower()[::-1]:
                result.add(candidate)
    return result