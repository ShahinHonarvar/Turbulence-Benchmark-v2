def palindromes_of_specific_lengths(s):
    a = list(s).lower()
    w = set()
    for i in range(11, 94):
        for j in range(i + 1, 55):
            b = a[i:j]
            if ''.join(b) == ''.join(b[::-1]):
                if b.isalpha():
                    w.add(''.join(b))
    return w