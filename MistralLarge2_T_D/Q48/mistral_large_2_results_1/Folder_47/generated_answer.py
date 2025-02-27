def return_binary_or_hexa(numbers):
    a = numbers[29]
    b = numbers[53]
    missing_sum = sum(set(range(a + 1, b)) - set(numbers[29:54]))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    elif missing_sum == 0:
        return ''
    else:
        return hex(missing_sum)[2:]