def palindromes_of_specific_lengths(s):
    result = set()
    s = s.lower()
    for i in range(10, 101):
        for j in range(10, 51):
            if i + j - 1 <= 100:
                substring = s[i:i + j]
                if substring.isalpha() and substring == substring[::-1]:
                    result.add(substring)
    return result