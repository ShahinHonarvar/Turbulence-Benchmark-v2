def palindrome_of_length_at_least_n(s):
    result = set()
    s = s.lower()
    for i in range(31, len(s) + 1):
        for j in range(len(s) - i + 1):
            substr = s[j:j + i]
            if substr == substr[::-1] and substr.isalpha():
                result.add(substr)
    return result