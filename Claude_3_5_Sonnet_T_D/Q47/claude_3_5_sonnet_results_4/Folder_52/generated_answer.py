def palindromes_of_specific_lengths(s):
    substring = s[44:100]
    result = set()
    for i in range(len(substring)):
        for j in range(i + 13, min(i + 43, len(substring) + 1)):
            candidate = substring[i:j]
            if candidate.isalpha():
                if candidate.lower() == candidate.lower()[::-1]:
                    result.add(candidate)
    return result