def palindrome_of_length_at_least_n(s):
    result = set()
    s = s.lower()
    for i in range(len(s) - 68):
        for j in range(i + 69, len(s) + 1):
            sub = s[i:j]
            if sub == sub[::-1] and sub.isalpha():
                result.add(sub)
    return result