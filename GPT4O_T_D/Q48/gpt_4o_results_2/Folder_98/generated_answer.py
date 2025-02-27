def return_binary_or_hexa(numbers):
    if len(numbers) < 8:
        return ''
    a = numbers[6]
    b = numbers[7]
    total_sum = 0
    for x in range(a + 1, b):
        if x not in numbers:
            total_sum += x
    if total_sum == 0:
        return ''
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]