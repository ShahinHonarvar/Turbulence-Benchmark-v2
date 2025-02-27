def return_binary_or_hexa(numbers):
    a = numbers[46]
    b = numbers[91]
    missing = [x for x in range(a + 1, b) if x not in numbers]
    if not missing:
        return ''
    s = sum(missing)
    if s % 2 != 0:
        return bin(s)[2:]
    else:
        return hex(s)[2:]