def return_binary_or_hexa(t):
    a = t[7]
    b = t[9]
    integers = set(range(a + 1, b))
    integers_in_tuple = set(t[7:10])
    missing_integers = integers - integers_in_tuple
    sum_missing = sum(missing_integers)
    if all((i in t[7:10] for i in range(a + 1, b))):
        return ''
    elif sum_missing % 2:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]