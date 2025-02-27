def return_binary_or_hexa(numbers):
    a = numbers[0]
    b = numbers[10]
    total = sum((x for x in range(a + 1, b) if x not in numbers[:11]))
    if total == 0:
        return ''
    if total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]