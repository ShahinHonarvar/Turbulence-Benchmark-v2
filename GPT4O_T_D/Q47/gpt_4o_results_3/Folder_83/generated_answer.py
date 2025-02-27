def palindromes_of_specific_lengths(s):
    s = s[75:96].lower()
    results = set()
    for length in range(7, 10):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if substring.isalpha() and substring == substring[::-1]:
                results.add(substring)
    return results