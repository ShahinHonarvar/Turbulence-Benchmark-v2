def return_binary_or_hexa(numbers):
    a = numbers[56]
    b = numbers[90]
    sum = 0
    for i in range(a + 1, b):
        if i not in numbers[56:90]:
            sum += i
    if sum % 2 != 0:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:]