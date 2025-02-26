def palindromes_of_specific_lengths(s):
    result = set()
    sub_s = s[28:95].lower()
    for length in range(38, 50):
        for start in range(len(sub_s) - length + 1):
            substring = sub_s[start:start + length]
            if all((c.isalpha() for c in substring)):
                if substring == substring[::-1]:
                    result.add(substring)
    return result