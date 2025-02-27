def palindromes_of_specific_lengths(s):
    result = set()
    for i in range(15, 96):
        for j in range(i + 20, min(i + 67, len(s) + 1)):
            substring = s[i:j].lower()
            if substring == substring[::-1]:
                if all((c.isalpha() for c in substring)):
                    result.add(substring)
    return result