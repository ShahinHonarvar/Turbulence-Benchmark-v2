def return_binary_or_hexa(tuple_of_integers):
    a = tuple_of_integers[18]
    b = tuple_of_integers[60]
    subset = set(tuple_of_integers[18:61])
    missing_sum = sum((i for i in range(a + 1, b) if i not in subset))
    if missing_sum == 0:
        return ''
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]