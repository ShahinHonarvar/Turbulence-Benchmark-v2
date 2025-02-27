def palindromes_of_specific_lengths(s):
    s = s[31:72].lower()
    result = set()
    for length in range(21, 33):
        for start in range(len(s) - length + 1):
            substring = s[start:start + length]
            if substring == substring[::-1]:
                if substring.isalpha():
                    result.add(substring)
    return result