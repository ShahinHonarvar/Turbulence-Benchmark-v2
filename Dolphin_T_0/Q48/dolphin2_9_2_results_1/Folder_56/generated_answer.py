def return_binary_or_hexa(t):
    a = t[7]
    b = t[9]
    not_in_tuple = [x for x in range(a + 1, b) if x not in t[7:10]]
    s = sum(not_in_tuple)
    if s % 2 == 1:
        return bin(s)[2:]
    else:
        return hex(s)[2:]