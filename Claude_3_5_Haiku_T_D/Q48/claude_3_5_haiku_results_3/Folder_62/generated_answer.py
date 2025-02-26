def return_binary_or_hexa(tuple_input):
    a = tuple_input[50]
    b = tuple_input[92]
    missing_numbers = []
    for num in range(a + 1, b):
        if num not in tuple_input[50:93]:
            missing_numbers.append(num)
    if not missing_numbers:
        return ''
    total_sum = sum(missing_numbers)
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]