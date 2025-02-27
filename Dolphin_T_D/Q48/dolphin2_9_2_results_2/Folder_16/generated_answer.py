def return_binary_or_hexa(input_tuple):
    a = input_tuple[90]
    b = input_tuple[97]
    missing_numbers = []
    for num in range(a + 1, b):
        if num not in input_tuple[90:98]:
            missing_numbers.append(num)
    if missing_numbers:
        total_sum = sum(missing_numbers)
        if total_sum % 2 != 0:
            return bin(total_sum)[2:]
        else:
            return hex(total_sum)[2:].upper()
    else:
        return ''