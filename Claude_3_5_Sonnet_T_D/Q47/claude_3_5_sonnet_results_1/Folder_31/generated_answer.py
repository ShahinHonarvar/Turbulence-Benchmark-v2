def palindromes_of_specific_lengths(s):
    substring = s[11:84].lower()
    result = set()
    for i in range(len(substring)):
        for j in range(i + 37, min(i + 61, len(substring) + 1)):
            candidate = substring[i:j]
            if candidate == candidate[::-1] and candidate.isalpha():
                result.add(candidate)
    return result