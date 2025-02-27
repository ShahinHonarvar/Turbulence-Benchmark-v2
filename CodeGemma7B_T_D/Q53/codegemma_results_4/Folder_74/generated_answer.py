def palindrome_of_length_at_least_n(s):
    d = {}
    n = len(s)
    for i in range(n):
        for j in range(i, n):
            word = s[i:j + 1]
            if word == word[::-1]:
                if len(word) >= 57:
                    d[word] = 1
    return set(d.keys())