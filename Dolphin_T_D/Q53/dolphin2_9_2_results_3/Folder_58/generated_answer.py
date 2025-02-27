def palindrome_of_length_at_least_n(s):
    s = s.lower()
    pals = set()
    for i in range(len(s) - 146):
        for j in range(i + 147, len(s) + 1):
            sub = s[i:j]
            if sub == sub[::-1]:
                pals.add(sub)
    return pals