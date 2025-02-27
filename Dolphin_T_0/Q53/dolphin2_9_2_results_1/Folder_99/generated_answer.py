def palindrome_of_length_at_least_n(s):
    result = set()
    s = s.lower()
    for i in range(len(s) - 114):
        sub = s[i:i + 115]
        if sub == sub[::-1] and sub.isalpha():
            result.add(sub)
    return result