def return_binary_or_hexa(numbers):
    a = numbers[27]
    b = numbers[96]
    missing_sum = sum((x for x in range(a + 1, b) if x not in numbers[28:96]))
    if missing_sum == 0:
        return ''
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]