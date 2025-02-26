def palindromes_of_specific_lengths(s):
    s = s.lower()
    result = set()
    start, end = (39, 94)
    for length in range(14, 53):
        for i in range(start, end - length + 2):
            substring = s[i:i + length]
            if len(substring) == length and substring == substring[::-1] and substring.isalpha():
                result.add(substring)
    return result