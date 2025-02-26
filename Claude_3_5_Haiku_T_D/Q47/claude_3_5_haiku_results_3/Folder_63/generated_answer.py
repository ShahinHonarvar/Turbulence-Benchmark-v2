def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[33:86]
    for length in range(26, 32):
        for i in range(len(substring) - length + 1):
            candidate = substring[i:i + length]
            if candidate.lower() == candidate.lower()[::-1] and candidate.isalpha():
                result.add(candidate)
    return result