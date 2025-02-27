def palindromes_of_specific_lengths(s):
    result = set()
    for i in range(20, 75):
        for j in range(i, 75):
            substring = s[i:j + 1]
            if 36 <= len(substring) <= 42:
                substring = substring.lower()
                if substring == substring[::-1] and substring.isalpha():
                    result.add(substring)
    return result