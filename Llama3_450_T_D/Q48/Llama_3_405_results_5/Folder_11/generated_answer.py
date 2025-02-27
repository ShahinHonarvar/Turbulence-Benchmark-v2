def return_binary_or_hexa(tuple_of_integers):
    a = tuple_of_integers[48]
    b = tuple_of_integers[76]
    existing_numbers = set(tuple_of_integers[49:76])
    total_sum = sum((i for i in range(a + 1, b) if i not in existing_numbers))
    if total_sum == 0:
        return ''
    elif total_sum % 2 != 0:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]