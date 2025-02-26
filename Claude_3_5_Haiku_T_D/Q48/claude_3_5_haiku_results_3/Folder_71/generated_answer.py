def return_binary_or_hexa(input_tuple):
    a = input_tuple[20]
    b = input_tuple[35]
    missing_numbers = []
    for num in range(a + 1, b):
        if num not in input_tuple[20:36]:
            missing_numbers.append(num)
    if not missing_numbers:
        return ''
    total_sum = sum(missing_numbers)
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]