def palindromes_of_specific_lengths(value):
    a = value[10:76]
    d = set()
    for b in range(10, 21):
        for c in range(len(a) - b + 1):
            e = a[c:c + b].lower()
            if e == e[::-1] and e.isalpha():
                d.add(e)
    return d