def palindrome_of_length_at_least_n(s):
    s = s.lower()
    result = set()
    length = len(s)
    for i in range(length):
        for j in range(i + 36, length):
            sub = s[i:j + 1]
            if sub == sub[::-1]:
                result.add(sub)
    return result