def return_binary_or_hexa(tuple_of_integers):
    a = tuple_of_integers[42]
    b = tuple_of_integers[87]
    subset = set(tuple_of_integers[42:88])
    total_sum = sum((i for i in range(a + 1, b) if i not in subset))
    if total_sum == 0:
        return ''
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:].upper()