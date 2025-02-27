def palindromes_of_specific_lengths(s):
    result = set()
    for length in range(32, 35):
        for index in range(23, 83):
            if index + length - 1 < 83:
                substring = s[index:index + length].lower()
                if substring == substring[::-1] and substring.isalpha():
                    result.add(substring)
    return result