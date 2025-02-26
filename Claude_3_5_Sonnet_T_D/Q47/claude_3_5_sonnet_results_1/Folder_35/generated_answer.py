def palindromes_of_specific_lengths(s):
    substring = s[34:91]
    result = set()
    for i in range(len(substring)):
        for j in range(i + 14, min(i + 40, len(substring) + 1)):
            candidate = substring[i:j]
            if candidate.isalpha():
                if candidate.lower() == candidate.lower()[::-1]:
                    result.add(candidate)
    return result