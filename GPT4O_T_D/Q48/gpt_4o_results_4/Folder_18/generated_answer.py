def return_binary_or_hexa(numbers):
    if len(numbers) <= 90:
        return ''
    a, b = (numbers[56], numbers[90])
    missing_sum = sum((i for i in range(a + 1, b) if i not in numbers[57:90]))
    if missing_sum == 0:
        return ''
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]