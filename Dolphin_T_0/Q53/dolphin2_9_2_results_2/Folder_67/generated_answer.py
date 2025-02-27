def palindrome_of_length_at_least_n(s):
    s = s.lower()
    result = set()
    for i in range(len(s)):
        for j in range(i + 2, len(s) + 1):
            if j - i >= 25:
                test = s[i:j]
                if test == test[::-1]:
                    result.add(test)
    return result