def return_binary_or_hexa(numbers):
    a = numbers[62]
    b = numbers[96]
    missing_sum = 0
    for num in range(a + 1, b):
        if num not in numbers[62:97]:
            missing_sum += num
    if missing_sum == 0:
        return ''
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]