def palindromes_of_specific_lengths(s):
    result = set()
    s = s.lower()
    for i in range(10, 101):
        for j in range(i, 101):
            substr = s[i:j + 1]
            if substr == substr[::-1] and substr.isalpha() and (10 <= len(substr) <= 50):
                result.add(substr)
    return result