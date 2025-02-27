def return_binary_or_hexa(numbers):
    if len(numbers) <= 88:
        return ''
    a = numbers[17]
    b = numbers[88]
    missing_sum = sum((i for i in range(a + 1, b) if i not in numbers[18:88]))
    if missing_sum == 0:
        return ''
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]