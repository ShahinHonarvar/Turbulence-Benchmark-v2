def return_binary_or_hexa(numbers):
    a = numbers[2]
    b = numbers[7]
    missing_sum = 0
    for num in range(a + 1, b):
        if num not in numbers[2:8]:
            missing_sum += num
    if missing_sum == 0:
        return ''
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]