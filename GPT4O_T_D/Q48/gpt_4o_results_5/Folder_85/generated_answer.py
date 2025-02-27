def return_binary_or_hexa(numbers):
    a = numbers[1]
    b = numbers[8]
    missing_numbers_sum = 0
    for num in range(a + 1, b):
        if num not in numbers[2:8]:
            missing_numbers_sum += num
    if missing_numbers_sum == 0:
        return ''
    if missing_numbers_sum % 2 == 1:
        return bin(missing_numbers_sum)[2:]
    return hex(missing_numbers_sum)[2:]