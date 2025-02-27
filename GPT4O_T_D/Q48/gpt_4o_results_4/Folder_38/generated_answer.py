def return_binary_or_hexa(numbers):
    if len(numbers) < 86:
        return ''
    a = numbers[36]
    b = numbers[85]
    missing_sum = 0
    current_set = set(numbers[36:86])
    for num in range(a + 1, b):
        if num not in current_set:
            missing_sum += num
    if missing_sum == 0:
        return ''
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]