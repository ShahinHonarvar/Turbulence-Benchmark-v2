def palindromes_of_specific_lengths(s):
    s = s.lower()
    result = set()
    for start in range(12, 57):
        for length in [20, 21]:
            if start + length > len(s):
                break
            substr = s[start:start + length]
            if all((char.isalpha() for char in substr)) and substr == substr[::-1]:
                result.add(substr)
    return result