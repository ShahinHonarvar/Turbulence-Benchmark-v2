def palindrome_of_length_n(word):
    x = set()
    for a in range(len(word)):
        for b in range(a + 1, len(word)):
            if word[a:b + 1][::-1] == word[a:b + 1]:
                if word[a:b + 1][:].lower() in x:
                    pass
                else:
                    x.add(word[a:b + 1][:])
    return x