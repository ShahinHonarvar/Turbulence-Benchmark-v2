def return_binary_or_hexa(numbers):
    a = numbers[427]
    b = numbers[669]
    total = 0
    for i in range(a + 1, b):
        if i not in numbers[427:669]:
            total += i
    if total % 2 != 0:
        return bin(total)[2:]
    else:
        return hex(total)[2:]