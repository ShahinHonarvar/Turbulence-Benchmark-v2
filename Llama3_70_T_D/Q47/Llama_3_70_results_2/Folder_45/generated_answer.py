def palindromes_of_specific_lengths(s):
    result = set()
    s = s[70:141].lower()
    for length in range(3, 61):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if substring.isalpha() and substring == substring[::-1]:
                result.add(substring)
    return result