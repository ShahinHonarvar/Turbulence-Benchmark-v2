def palindrome_of_length_n(s):
    s = s.lower()
    n = 34
    palindrome_set = set()
    for i in range(len(s) - n + 1):
        sub = s[i:i + n]
        if sub == sub[::-1]:
            if sub.isalpha():
                palindrome_set.add(sub)
    return palindrome_set