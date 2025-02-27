def palindrome_of_length_n(s):
    s = s.lower()
    palindrome_set = set()
    for i in range(len(s) - 14):
        sub = s[i:i + 15]
        if sub == sub[::-1] and sub.isalpha():
            palindrome_set.add(sub)
    return palindrome_set