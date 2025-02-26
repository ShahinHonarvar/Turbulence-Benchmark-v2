def palindromes_of_specific_lengths(s):
    result = set()
    s = s.lower()
    substring = s[27:78]
    for i in range(len(substring) - 17):
        for length in range(18, 20):
            if i + length > len(substring):
                break
            candidate = substring[i:i + length]
            if candidate == candidate[::-1] and candidate.isalpha():
                result.add(candidate)
    return result