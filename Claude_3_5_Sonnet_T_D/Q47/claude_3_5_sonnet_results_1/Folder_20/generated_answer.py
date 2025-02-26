def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[20:75]
    for i in range(len(substring)):
        for j in range(i + 36, min(i + 43, len(substring) + 1)):
            candidate = substring[i:j]
            if candidate.isalpha() and candidate.lower() == candidate.lower()[::-1]:
                result.add(candidate)
    return result