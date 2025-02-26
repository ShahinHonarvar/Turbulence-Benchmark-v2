def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[21:63]
    for i in range(len(substring)):
        for j in range(i + 22, i + 34):
            if j <= len(substring):
                candidate = substring[i:j]
                if candidate.isalpha():
                    if candidate.lower() == candidate.lower()[::-1]:
                        result.add(candidate)
    return result