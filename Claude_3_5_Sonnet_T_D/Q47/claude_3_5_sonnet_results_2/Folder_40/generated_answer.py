def palindromes_of_specific_lengths(s):
    result = set()
    s = s[:6].lower()
    for i in range(6):
        for j in range(i + 3, min(i + 6, 7)):
            substr = s[i:j]
            if substr.isalpha() and substr == substr[::-1]:
                result.add(substr)
    return result