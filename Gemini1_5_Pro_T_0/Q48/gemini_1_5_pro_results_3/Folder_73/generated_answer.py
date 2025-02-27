def return_binary_or_hexa(numbers):
    a = numbers[10]
    b = numbers[76]
    sum = 0
    for i in range(a + 1, b):
        if i not in numbers[10:77]:
            sum += i
    if sum % 2 == 1:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:]