def return_binary_or_hexa(numbers):
    if len(numbers) <= 84:
        return ''
    a = numbers[57]
    b = numbers[84]
    missing_sum = sum((i for i in range(a + 1, b) if i not in numbers[58:84]))
    if missing_sum == 0:
        return ''
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]