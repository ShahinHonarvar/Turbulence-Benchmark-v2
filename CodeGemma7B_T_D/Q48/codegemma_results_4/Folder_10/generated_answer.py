def return_binary_or_hexa(numbers):
    a = numbers[36]
    b = numbers[54]
    sum = 0
    for i in range(a + 1, b):
        if i not in numbers[36:55]:
            sum += i
    if sum % 2 == 0:
        return hex(sum)[2:].upper()
    else:
        return bin(sum)[2:]