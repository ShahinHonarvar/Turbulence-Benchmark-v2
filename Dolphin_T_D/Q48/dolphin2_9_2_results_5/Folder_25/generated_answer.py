def return_binary_or_hexa(t):
    a = t[37]
    b = t[43]
    numbers = sets(range(a + 1, b))
    tuple_numbers = set(t[38:43])
    missing_numbers = numbers - tuple_numbers
    sum_numbers = sum(missing_numbers)
    if sum_numbers % 2 == 0:
        return hex(sum_numbers)[2:].upper()
    else:
        return bin(sum_numbers)[2:]
    if not missing_numbers:
        return ''