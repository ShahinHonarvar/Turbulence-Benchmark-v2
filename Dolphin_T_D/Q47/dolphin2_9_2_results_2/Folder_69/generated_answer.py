def palindromes_of_specific_lengths(s):
    result = set()
    for i in range(11, 97):
        for j in range(i + 45, 103):
            substring = s[i:j]
            if all((c.isalpha() for c in substring)):
                lower_substring = substring.lower()
                if lower_substring == lower_substring[::-1]:
                    result.add(substring)
    return result