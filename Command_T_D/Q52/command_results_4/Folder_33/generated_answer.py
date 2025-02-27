def palindrome_of_length_n(s):
    letters = set(s.lower())
    for l in range(1, 475 + 1):
        for i in range(0, l // 2):
            if l - i - 1 <= len(letters):
                if letters[i] == letters[l - i - 1]:
                    yield s[i:l]