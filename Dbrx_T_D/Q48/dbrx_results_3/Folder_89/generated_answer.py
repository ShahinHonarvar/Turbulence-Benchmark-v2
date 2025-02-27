def return_binary_or_hexa(numbers):
    a = numbers[55]
    b = numbers[84]
    sum = 0
    for i in range(a + 1, b):
        if i not in numbers[55:85]:
            sum += i
    if sum % 2 != 0:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:].upper()