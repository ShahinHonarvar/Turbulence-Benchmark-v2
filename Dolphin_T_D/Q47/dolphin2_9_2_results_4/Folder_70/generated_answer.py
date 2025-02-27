def palindromes_of_specific_lengths(s):
    s = s[10:70].lower()
    result = set()
    for length in range(24, 53):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if all((c.isalpha() for c in substring)) and substring == substring[::-1]:
                result.add(substring)
    return result