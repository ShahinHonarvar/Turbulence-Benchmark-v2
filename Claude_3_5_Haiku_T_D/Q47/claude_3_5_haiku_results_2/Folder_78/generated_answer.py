def palindromes_of_specific_lengths(s):
    s = s.lower()
    result = set()
    for i in range(15, 73):
        for j in range(i + 18, min(i + 56, len(s) + 1)):
            substring = s[i:j]
            if substring == substring[::-1] and substring.isalpha():
                result.add(substring)
    return result