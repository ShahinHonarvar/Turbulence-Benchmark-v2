def return_binary_or_hexa(tup):
    a = tup[42]
    b = tup[87]
    existing_numbers = set(tup[42:88])
    sum_result = sum((num for num in range(a + 1, b) if num not in existing_numbers))
    if sum_result == 0:
        return ''
    elif sum_result % 2 == 1:
        return bin(sum_result)[2:]
    else:
        return hex(sum_result)[2:]