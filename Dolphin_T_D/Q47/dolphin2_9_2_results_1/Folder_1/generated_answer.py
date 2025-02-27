def palindromes_of_specific_lengths(s):
    result = set()
    for length in range(40, 73):
        for i in range(15, 90):
            substring = s[i:i + length]
            if substring == substring[::-1]:
                result.add(substring.lower())
    return result