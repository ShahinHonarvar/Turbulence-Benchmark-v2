def return_binary_or_hexa(numbers):
    a = numbers[13]
    b = numbers[91]
    missing_sum = 0
    for num in range(a + 1, b):
        if num not in numbers[14:92]:
            missing_sum += num
    if missing_sum == 0:
        return ''
    return bin(missing_sum)[2:] if missing_sum % 2 else hex(missing_sum)[2:]