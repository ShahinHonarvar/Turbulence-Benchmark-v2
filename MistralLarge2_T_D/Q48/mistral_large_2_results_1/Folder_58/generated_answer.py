def return_binary_or_hexa(numbers):
    a = numbers[275]
    b = numbers[871]
    subset = set(numbers[275:872])
    missing_sum = sum((x for x in range(a + 1, b) if x not in subset))
    if missing_sum == 0:
        return ''
    elif missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]