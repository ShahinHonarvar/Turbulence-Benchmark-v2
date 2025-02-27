def palindromes_between_indices(s):
    result = set()
    for start in range(4, 8):
        for end in range(start, 8):
            substring = s[start:end + 1].lower()
            if len(substring) >= 5 and substring == substring[::-1]:
                result.add(substring)
    return result