def return_binary_or_hexa(tuple_input):
    a = tuple_input[56]
    b = tuple_input[88]
    excluded_numbers = set(tuple_input[57:88])
    sum_result = sum((num for num in range(a + 1, b) if num not in excluded_numbers))
    if sum_result == 0:
        return ''
    if sum_result % 2 == 1:
        return bin(sum_result)[2:]
    else:
        return hex(sum_result)[2:].rstrip('L')