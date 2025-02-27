def palindrome_of_length_at_least_n(s):
    scl = s.lower()
    n = 77
    poss = set()
    for i in range(len(scl)):
        for j in range(i + n - 1, len(scl)):
            word = scl[i:j + 1]
            word = ''.join(set(word))
            if word == word[::-1]:
                if len(word) >= n:
                    poss.add(word)
    return poss