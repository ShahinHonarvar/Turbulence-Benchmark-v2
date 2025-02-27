def palindromes_of_specific_lengths(s):
    if len(s) < 301:
        return set()
    result = set()
    substring = s[100:301].lower()
    for start in range(len(substring)):
        for end in range(start + 50, min(start + 101, len(substring) + 1)):
            candidate = substring[start:end]
            if candidate == candidate[::-1] and candidate.isalpha():
                result.add(candidate)
    return result