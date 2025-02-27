def return_binary_or_hexa(numbers):
    a, b = (numbers[86], numbers[90])
    missing_sum = sum(set(range(a + 1, b)) - set(numbers[86:91]))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    elif missing_sum == 0:
        return ''
    else:
        return hex(missing_sum)[2:]