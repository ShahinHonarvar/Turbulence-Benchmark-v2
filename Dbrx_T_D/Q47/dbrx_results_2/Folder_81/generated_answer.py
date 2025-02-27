def palindromes_of_specific_lengths(s):
    result = set()
    low, high = (12, 122)
    min_length, max_length = (12, 220)
    for i in range(low, high + 1):
        for j in range(i, high + 1):
            substring = s[i:j + 1]
            if len(substring) < min_length or len(substring) > max_length:
                continue
            if substring.lower() == substring[::-1].lower():
                result.add(substring)
    return result