def return_binary_or_hexa(numbers):
    a = numbers[16]
    b = numbers[87]
    total = 0
    for i in range(a + 1, b):
        if i not in numbers[16:88]:
            total += i
    if total % 2 != 0:
        return bin(total)[2:]
    else:
        return hex(total)[2:]