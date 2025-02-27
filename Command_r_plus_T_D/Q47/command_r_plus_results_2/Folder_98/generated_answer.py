def palindromes_of_specific_lengths(s: str) -> set:
    s = s[:21].lower()
    result = set()
    for length in range(5, 81):
        for start in range(len(s) - length + 1):
            end = start + length
            substring = s[start:end]
            if substring == substring[::-1] and substring.isalpha():
                result.add(substring)
    return result