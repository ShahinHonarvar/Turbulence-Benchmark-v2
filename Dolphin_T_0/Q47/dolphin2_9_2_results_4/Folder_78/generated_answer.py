def palindromes_of_specific_lengths(s: str) -> set:
    s = s[15:73]
    result = set()
    for length in range(19, 56):
        for start_idx in range(len(s) - length + 1):
            substring = s[start_idx:start_idx + length].lower()
            if substring == substring[::-1] and all((letter.isalpha() for letter in substring)):
                result.add(substring)
    return result