def palindromes_of_specific_lengths(s):
    result = set()
    for start in range(130, 296):
        for length in range(103, 159):
            end = start + length
            if end > len(s):
                break
            substring = s[start:end].lower()
            if substring == substring[::-1] and substring.isalpha():
                result.add(substring)
    return result