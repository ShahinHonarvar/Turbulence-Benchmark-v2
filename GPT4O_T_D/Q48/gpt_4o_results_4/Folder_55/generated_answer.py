def return_binary_or_hexa(numbers):
    a = numbers[10]
    b = numbers[12]
    missing_sum = sum((n for n in range(a + 1, b) if n not in numbers[11:12]))
    if not missing_sum:
        return ''
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    return hex(missing_sum)[2:]