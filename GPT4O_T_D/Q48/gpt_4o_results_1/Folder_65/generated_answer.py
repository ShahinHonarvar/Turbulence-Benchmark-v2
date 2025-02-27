def return_binary_or_hexa(numbers):
    if len(numbers) <= 76:
        return ''
    a = numbers[51]
    b = numbers[76]
    total_sum = 0
    missing = False
    for num in range(a + 1, b):
        if num not in numbers[52:76]:
            total_sum += num
            missing = True
    if not missing:
        return ''
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]