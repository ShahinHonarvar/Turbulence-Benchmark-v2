def palindrome_of_length_at_least_n(s):
    result = set()
    s = s.lower()
    for i in range(len(s) - 99):
        sub = s[i:i + 100]
        if sub == sub[::-1]:
            result.add(sub)
    return result