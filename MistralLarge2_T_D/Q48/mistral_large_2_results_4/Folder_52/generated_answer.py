def return_binary_or_hexa(numbers):
    a, b = (numbers[38], numbers[81])
    missing_sum = sum((x for x in range(a + 1, b) if x not in numbers[38:82]))
    if missing_sum == 0:
        return ''
    elif missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]