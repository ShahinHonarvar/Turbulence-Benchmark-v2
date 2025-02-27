def palindrome_of_length_n(s):
    n = 16
    result = set()
    for i in range(len(s) - n + 1):
        sub = s[i:i + n].lower()
        if sub == sub[::-1] and sub.isalpha():
            result.add(sub)
    return result