def palindromes_of_specific_lengths(s):
    result = set()
    s = s[:11].lower()
    for i in range(11):
        for j in range(i + 3, min(i + 6, 12)):
            substr = s[i:j]
            if substr == substr[::-1] and substr.isalpha():
                result.add(substr)
    return result