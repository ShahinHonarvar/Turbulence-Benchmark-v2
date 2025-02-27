def return_binary_or_hexa(numbers):
    if len(numbers) < 6:
        return ''
    a = numbers[2]
    b = numbers[5]
    missing_sum = sum((i for i in range(a + 1, b) if i not in numbers[2:6]))
    if missing_sum == 0:
        return ''
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]