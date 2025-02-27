def return_binary_or_hexa(numbers):
    a = numbers[32]
    b = numbers[44]
    total_sum = 0
    for num in range(a + 1, b):
        if num not in numbers[32:45]:
            total_sum += num
    if total_sum == 0:
        return ''
    if total_sum % 2 != 0:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:].upper()