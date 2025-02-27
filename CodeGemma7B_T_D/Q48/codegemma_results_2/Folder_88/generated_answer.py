def return_binary_or_hexa(tup):
    a, b = (tup[3], tup[9])
    k = 0
    for i in range(a + 1, b):
        if i in tup[3:10]:
            continue
        else:
            k += i
    if k % 2:
        return str(k)[2:].lower()
    else:
        return hex(k)[2:].lower()