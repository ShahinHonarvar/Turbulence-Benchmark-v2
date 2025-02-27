def return_binary_or_hexa(numbers):
    a = numbers[44]
    b = numbers[91]
    missing_sum = 0
    num_set = set(numbers[45:91])
    for number in range(a + 1, b):
        if number not in num_set:
            missing_sum += number
    if missing_sum == 0:
        return ''
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:].lower()