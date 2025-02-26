def palindromes_of_specific_lengths(s):
    substring = s[101:293]
    result = set()
    for i in range(len(substring)):
        for j in range(i + 154, min(i + 183, len(substring) + 1)):
            candidate = substring[i:j]
            if candidate.isalpha() and candidate.lower() == candidate.lower()[::-1]:
                result.add(candidate)
    return result