def return_binary_or_hexa(numbers):
    a = numbers[44]
    b = numbers[67]
    missing_sum = sum((i for i in range(a + 1, b) if i not in numbers[45:67]))
    if missing_sum == 0:
        return ''
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]