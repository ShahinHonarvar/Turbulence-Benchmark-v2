def return_binary_or_hexa(numbers):
    a = numbers[46]
    b = numbers[91]
    total = 0
    for num in range(a + 1, b):
        if num not in numbers[46:92]:
            total += num
    if total % 2 != 0:
        return bin(total)[2:]
    else:
        return hex(total)[2:]