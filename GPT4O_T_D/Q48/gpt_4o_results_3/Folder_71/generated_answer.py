def return_binary_or_hexa(numbers):
    a = numbers[20]
    b = numbers[35]
    current_range = set(numbers[21:35])
    calculation_sum = sum((i for i in range(a + 1, b) if i not in current_range))
    if calculation_sum == 0:
        return ''
    if calculation_sum % 2:
        return bin(calculation_sum)[2:]
    else:
        return hex(calculation_sum)[2:]