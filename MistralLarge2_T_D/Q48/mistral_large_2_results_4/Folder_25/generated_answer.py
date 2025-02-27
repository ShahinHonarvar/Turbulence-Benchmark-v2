def return_binary_or_hexa(numbers):
    a, b = (numbers[37], numbers[43])
    subset = set(numbers[37:44])
    missing_sum = sum((x for x in range(a + 1, b) if x not in subset))
    if missing_sum == 0:
        return ''
    elif missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:].upper()