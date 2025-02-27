def return_binary_or_hexa(numbers):
    a = numbers[2]
    b = numbers[5]
    sum = 0
    for i in range(a + 1, b):
        if i not in numbers[2:5]:
            sum += i
    if sum % 2:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:]