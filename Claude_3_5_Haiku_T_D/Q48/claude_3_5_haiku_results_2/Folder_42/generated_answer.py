def return_binary_or_hexa(numbers):
    a = numbers[18]
    b = numbers[60]
    missing_numbers_sum = 0
    for num in range(a + 1, b):
        if num not in numbers[18:61]:
            missing_numbers_sum += num
    if missing_numbers_sum == 0:
        return ''
    if missing_numbers_sum % 2 == 1:
        return bin(missing_numbers_sum)[2:]
    else:
        return hex(missing_numbers_sum)[2:]