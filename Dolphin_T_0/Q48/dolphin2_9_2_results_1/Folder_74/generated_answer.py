def return_binary_or_hexa(numbers):
    a = numbers[69]
    b = numbers[97]
    total = 0
    for i in range(a + 1, b):
        if not numbers[69:98].count(i):
            total += i
    if total % 2:
        return bin(total)[2:]
    else:
        return hex(total)[2:].upper()
    return ''