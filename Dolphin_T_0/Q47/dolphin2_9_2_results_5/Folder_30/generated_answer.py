def palindromes_of_specific_lengths(s):
    s = s[13:91]
    result = set()
    for length in range(55, 72):
        for i in range(len(s) - length + 1):
            substring = s[i:length + i]
            if all((c.isalpha() or c.isspace() for c in substring)) and substring.lower() == substring[::-1].lower():
                result.add(substring)
    return result