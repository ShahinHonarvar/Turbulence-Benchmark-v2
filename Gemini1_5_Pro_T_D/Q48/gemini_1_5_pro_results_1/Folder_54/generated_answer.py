def return_binary_or_hexa(numbers):
    a = numbers[35]
    b = numbers[64]
    total_sum = 0
    for num in range(a + 1, b):
        if num not in numbers[35:65]:
            total_sum += num
    if total_sum == 0:
        return ''
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:].upper()