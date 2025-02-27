def palindromes_of_specific_lengths(s):
    result = set()
    for i in range(40, 95):
        for j in range(i + 44, i + 52):
            if j < 95:
                substring = s[i:j].lower()
                if substring == substring[::-1] and substring.isalpha():
                    result.add(substring)
    return result