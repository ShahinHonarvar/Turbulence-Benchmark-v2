def palindromes_of_specific_lengths(s):
    result = set()
    for i in range(32, 80):
        for j in range(i + 34, i + 42):
            substring = s[i:j + 1]
            if substring == substring[::-1] and substring.isalpha():
                result.add(substring.lower())
    return result