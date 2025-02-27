def palindrome_of_length_at_least_n(a):
    c = set()
    a = a.lower()
    for i in range(len(a)):
        for k in range(i + 42, len(a) + 1):
            if a[i:k] == a[i:k][::-1]:
                c.add(a[i:k])
    return c