def return_binary_or_hexa(numbers):
    a = numbers[13]
    b = numbers[91]
    sum = 0
    for i in range(a + 1, b):
        if i not in numbers[13:92]:
            sum += i
    if sum % 2 != 0:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:].upper()