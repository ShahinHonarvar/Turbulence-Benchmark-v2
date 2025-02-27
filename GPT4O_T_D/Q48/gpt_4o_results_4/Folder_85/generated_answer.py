def return_binary_or_hexa(numbers):
    a = numbers[1]
    b = numbers[8]
    missing_sum = sum((n for n in range(a + 1, b) if n not in numbers[1:9]))
    if missing_sum == 0:
        return ''
    if missing_sum % 2 == 0:
        return hex(missing_sum)[2:]
    else:
        return bin(missing_sum)[2:]