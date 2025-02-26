def return_binary_or_hexa(input_tuple):
    a = input_tuple[90]
    b = input_tuple[200]
    subset = set(input_tuple[90:201])
    missing_sum = sum((num for num in range(a + 1, b) if num not in subset))
    if missing_sum == 0:
        return ''
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]