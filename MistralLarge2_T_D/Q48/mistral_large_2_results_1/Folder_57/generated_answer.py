def return_binary_or_hexa(tuple_of_integers):
    a = tuple_of_integers[25]
    b = tuple_of_integers[80]
    sub_tuple = tuple_of_integers[25:81]
    missing_sum = sum((i for i in range(a + 1, b) if i not in sub_tuple))
    if missing_sum == 0:
        return ''
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:].upper()