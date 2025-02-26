def return_binary_or_hexa(tuple_input):
    a = tuple_input[19]
    b = tuple_input[32]
    subset = set(tuple_input[19:33])
    total_sum = sum((num for num in range(a + 1, b) if num not in subset))
    if total_sum == 0:
        return ''
    elif total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]