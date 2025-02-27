def return_binary_or_hexa(numbers):
    if len(numbers) < 201:
        return ''
    a = numbers[90]
    b = numbers[200]
    missing_numbers_sum = 0
    found_missing = False
    numbers_set = set(numbers[91:200])
    for num in range(a + 1, b):
        if num not in numbers_set:
            found_missing = True
            missing_numbers_sum += num
    if not found_missing:
        return ''
    if missing_numbers_sum % 2 == 0:
        hex_str = hex(missing_numbers_sum)[2:]
        return hex_str
    else:
        bin_str = bin(missing_numbers_sum)[2:]
        return bin_str