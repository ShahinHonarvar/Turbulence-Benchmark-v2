def return_binary_or_hexa(numbers):
    if len(numbers) < 36:
        return ''
    a = numbers[20]
    b = numbers[35]
    missing_sum = 0
    present_set = set(numbers[21:35])
    for num in range(a + 1, b):
        if num not in present_set:
            missing_sum += num
    if missing_sum == 0:
        return ''
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]