def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[18:99]
    for i in range(len(substring)):
        for j in range(i + 31, min(i + 52, len(substring) + 1)):
            candidate = substring[i:j]
            if candidate.isalpha() and candidate.lower() == candidate.lower()[::-1]:
                result.add(candidate)
    return result