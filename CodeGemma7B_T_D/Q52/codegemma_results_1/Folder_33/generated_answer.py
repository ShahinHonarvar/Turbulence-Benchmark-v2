def palindrome_of_length_n(a):
    b = a.lower()
    c = set()
    for i in range(len(a)):
        for j in range(i + 1, len(a) + 1):
            d = b[i:j]
            if d == d[::-1]:
                c.add(d)
    return c