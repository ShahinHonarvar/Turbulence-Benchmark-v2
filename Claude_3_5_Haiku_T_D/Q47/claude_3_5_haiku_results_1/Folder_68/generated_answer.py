def palindromes_of_specific_lengths(s):
    result = set()
    s = s.lower()
    for start in range(51):
        for end in range(start + 49, start + 100):
            if end >= len(s):
                break
            substring = s[start:end + 1]
            if len(substring) >= 50 and len(substring) <= 100:
                if substring == substring[::-1] and substring.isalpha():
                    result.add(substring)
    return result