def palindromes_of_specific_lengths(s):
    substring = s[62:89]
    result = set()
    for i in range(len(substring)):
        for j in range(i + 18, min(i + 22, len(substring) + 1)):
            candidate = substring[i:j]
            if candidate.isalpha():
                if candidate.lower() == candidate.lower()[::-1]:
                    result.add(candidate)
    return result