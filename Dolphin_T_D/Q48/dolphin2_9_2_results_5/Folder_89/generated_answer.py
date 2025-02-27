def return_binary_or_hexa(tuples):
    a = tuples[55]
    b = tuples[84]
    integers = set(range(a + 1, b))
    tuple_integers = set(tuples[55:85])
    missing = integers - tuple_integers
    if not missing:
        return ''
    s = sum(missing)
    if s % 2:
        return bin(s)[2:]
    else:
        return hex(s)[2:]