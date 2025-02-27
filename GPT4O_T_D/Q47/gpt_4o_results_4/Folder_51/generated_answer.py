def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[2:9]
    length = len(substring)
    for start in range(length):
        for end in range(start + 3, min(start + 5, length + 1)):
            candidate = substring[start:end]
            if candidate.isalpha() and candidate.lower() == candidate.lower()[::-1]:
                result.add(candidate)
    return result