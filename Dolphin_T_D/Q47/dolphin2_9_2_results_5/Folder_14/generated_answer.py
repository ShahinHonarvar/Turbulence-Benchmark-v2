def palindromes_of_specific_lengths(s):
    result = set()
    for i in range(10, 75):
        for length in range(6, 9):
            substring = s[i:i + length]
            if substring == substring[::-1] and substring.isalpha():
                result.add(substring.lower())
    return result