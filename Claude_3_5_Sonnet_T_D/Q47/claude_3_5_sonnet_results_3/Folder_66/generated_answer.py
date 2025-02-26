def palindromes_of_specific_lengths(s):
    substring = s[32:80]
    result = set()
    for i in range(len(substring)):
        for j in range(i + 35, min(i + 42, len(substring) + 1)):
            candidate = substring[i:j]
            if candidate.isalpha() and candidate.lower() == candidate.lower()[::-1]:
                result.add(candidate)
    return result