def palindromes_of_specific_lengths(s):
    result = set()
    s = s.lower()
    start, end = (12, 56)
    if start >= len(s) or end >= len(s):
        return result
    substring = s[start:end + 1]
    for length in range(20, 22):
        for i in range(len(substring) - length + 1):
            candidate = substring[i:i + length]
            if len(candidate) == length and all((c.isalpha() for c in candidate)):
                if candidate == candidate[::-1]:
                    result.add(candidate)
    return result