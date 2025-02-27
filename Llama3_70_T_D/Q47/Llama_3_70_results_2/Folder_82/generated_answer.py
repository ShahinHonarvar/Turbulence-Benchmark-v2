def palindromes_of_specific_lengths(s):
    s = s[3:301].lower()
    result = set()
    for length in range(30, 301):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if substring == substring[::-1] and substring.isalpha():
                result.add(substring)
    return result