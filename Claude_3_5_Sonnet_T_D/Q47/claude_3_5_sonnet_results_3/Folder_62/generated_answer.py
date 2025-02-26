def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[26:88]
    for i in range(len(substring)):
        for j in range(i + 52, i + 57):
            if j <= len(substring):
                candidate = substring[i:j]
                if candidate.isalpha():
                    if candidate.lower() == candidate.lower()[::-1]:
                        result.add(candidate)
    return result