def return_binary_or_hexa(numbers):
    if len(numbers) <= 99:
        return ''
    a = numbers[32]
    b = numbers[99]
    missing_sum = sum((x for x in range(a + 1, b) if x not in numbers[33:100]))
    if missing_sum == 0:
        return ''
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]