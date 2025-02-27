def palindromes_of_specific_lengths(s):
    s = s.lower()
    result = set()
    for i in range(10, 75):
        for j in range(i + 5, min(i + 9, 75)):
            substr = s[i:j]
            if substr == substr[::-1] and substr.isalpha():
                result.add(substr)
    return result