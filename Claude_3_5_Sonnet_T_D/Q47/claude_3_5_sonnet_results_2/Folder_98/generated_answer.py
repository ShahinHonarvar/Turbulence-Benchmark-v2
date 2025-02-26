def palindromes_of_specific_lengths(s):
    result = set()
    s = s[:21].lower()
    for start in range(21):
        for end in range(start + 5, min(start + 81, 22)):
            substring = s[start:end]
            if substring.isalpha() and substring == substring[::-1]:
                result.add(substring)
    return result