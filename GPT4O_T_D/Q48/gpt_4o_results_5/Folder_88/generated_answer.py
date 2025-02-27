def return_binary_or_hexa(numbers):
    if len(numbers) < 10:
        return ''
    a = numbers[3]
    b = numbers[9]
    missing_numbers_sum = 0
    present_numbers_set = set(numbers[4:9])
    for num in range(a + 1, b):
        if num not in present_numbers_set:
            missing_numbers_sum += num
    if missing_numbers_sum == 0:
        return ''
    if missing_numbers_sum % 2 == 1:
        return bin(missing_numbers_sum)[2:]
    else:
        return hex(missing_numbers_sum)[2:]