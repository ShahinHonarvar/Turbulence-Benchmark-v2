def palindrome_of_length_n(text):
    txt = text.lower()
    s = set()
    for i in range(len(txt)):
        for j in range(i + 72, len(txt) + 1):
            sub = txt[i:j]
            sub = ''.join((c for c in sub if c.isalpha()))
            if sub == sub[::-1]:
                s.add(sub)
    return s