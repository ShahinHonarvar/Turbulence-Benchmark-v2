def palindromes_of_specific_lengths(s):
    result = set()
    s = s[:7].lower()
    for length in range(3, 7):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if substring.isalpha() and substring == substring[::-1]:
                result.add(substring)
    return result