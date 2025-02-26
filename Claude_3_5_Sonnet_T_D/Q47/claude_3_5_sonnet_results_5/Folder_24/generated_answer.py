def palindromes_of_specific_lengths(s):
    substring = s[12:93]
    result = set()
    for i in range(len(substring)):
        for j in range(i + 42, min(i + 78, len(substring) + 1)):
            candidate = substring[i:j]
            if candidate.isalpha() and candidate.lower() == candidate.lower()[::-1]:
                result.add(candidate)
    return result