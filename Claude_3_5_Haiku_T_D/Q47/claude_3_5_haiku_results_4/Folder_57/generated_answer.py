def palindromes_of_specific_lengths(s):
    s = s.lower()
    result = set()
    start = 16
    end = 94
    if start >= len(s) or end >= len(s):
        return result
    substring = s[start:end + 1]
    for length in range(39, 53):
        for i in range(len(substring) - length + 1):
            candidate = substring[i:i + length]
            if all((char.isalpha() for char in candidate)) and candidate == candidate[::-1]:
                result.add(candidate)
    return result