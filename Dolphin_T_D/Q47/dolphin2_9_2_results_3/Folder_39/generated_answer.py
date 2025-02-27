def palindromes_of_specific_lengths(s):
    result = set()
    s = s[30:92]
    for length in range(50, 54):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if substring == substring.lower() and substring == substring[::-1].lower():
                result.add(substring)
    return result