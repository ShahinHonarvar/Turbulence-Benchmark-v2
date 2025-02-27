def return_binary_or_hexa(numbers):
    a = numbers[46]
    b = numbers[91]
    missing_values_sum = sum((x for x in range(a + 1, b) if x not in numbers[47:91]))
    if missing_values_sum == 0:
        return ''
    if missing_values_sum % 2 == 1:
        return bin(missing_values_sum)[2:]
    else:
        return hex(missing_values_sum)[2:]