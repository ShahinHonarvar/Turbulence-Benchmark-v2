def return_binary_or_hexa(numbers):
    a, b = (numbers[56], numbers[88])
    existing = set(numbers[57:89])
    result = 0
    for i in range(a + 1, b):
        if i not in existing:
            result += i
    if result % 2 == 1:
        return bin(result)[2:]
    else:
        return hex(result)[2:]