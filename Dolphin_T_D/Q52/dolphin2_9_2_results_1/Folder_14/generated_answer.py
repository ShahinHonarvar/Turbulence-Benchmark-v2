def palindrome_of_length_n(s):
    s = s.lower()
    result = set()
    for i in range(len(s) - 62):
        sub = s[i:i + 63]
        if sub == sub[::-1] and set(sub).issubset('abcdefghijklmnopqrstuvwxyz'):
            result.add(sub)
    return result