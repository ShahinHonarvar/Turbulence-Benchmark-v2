def palindromes_of_specific_lengths(s):
    s = s[10:97]
    result = set()
    for length in range(29, 63):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if all((char.isalpha() for char in substring.lower())):
                if substring.lower() == substring.lower()[::-1]:
                    result.add(substring)
    return result