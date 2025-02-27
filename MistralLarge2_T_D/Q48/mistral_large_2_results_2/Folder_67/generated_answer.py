def return_binary_or_hexa(numbers):
    a, b = (numbers[44], numbers[67])
    missing_sum = 0
    present_set = set(numbers[44:68])
    for num in range(a + 1, b):
        if num not in present_set:
            missing_sum += num
    if missing_sum == 0:
        return ''
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]