def return_binary_or_hexa(numbers):
    a = numbers[49]
    b = numbers[74]
    missing_sum = 0
    num_set = set(numbers[49:75])
    for num in range(a + 1, b):
        if num not in num_set:
            missing_sum += num
    if missing_sum == 0:
        return ''
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]