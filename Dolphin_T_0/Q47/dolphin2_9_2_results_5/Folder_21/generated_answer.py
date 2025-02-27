def palindromes_of_specific_lengths(s):
    a = s[100:296]
    b = set()
    for i in range(136, 161):
        for j in range(len(a) - i + 1):
            c = a[j:j + i]
            d = ''.join((e for e in c if e.isalpha()))
            if d[::-1].lower() == d.lower():
                b.add(d)
    return b