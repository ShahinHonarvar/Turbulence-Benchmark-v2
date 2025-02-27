def palindromes_of_specific_lengths(s):
    s = s.lower()
    start, end = (1, 8)
    result = set()
    for i in range(start, end + 1):
        for length in [3, 4]:
            if i + length <= end + 1:
                substring = s[i:i + length]
                if substring == substring[::-1] and substring.isalpha():
                    result.add(substring)
    return result