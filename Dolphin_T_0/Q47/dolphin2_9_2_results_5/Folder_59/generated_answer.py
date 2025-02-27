def palindromes_of_specific_lengths(s):
    s = s[:101].lower()
    result = set()
    for length in range(3, 16):
        for start in range(0, 101 - length + 1):
            substring = s[start:start + length]
            if substring == substring[::-1] and all((character.isalpha() for character in substring)):
                result.add(substring)
    return result