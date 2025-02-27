def return_binary_or_hexa(numbers):
    a = numbers[1]
    b = numbers[4]
    sum = 0
    for i in range(a + 1, b):
        if i not in numbers[1:5]:
            sum += i
    if sum % 2 != 0:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:]