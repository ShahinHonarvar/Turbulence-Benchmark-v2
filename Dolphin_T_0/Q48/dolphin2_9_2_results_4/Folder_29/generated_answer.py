def return_binary_or_hexa(numbers):
    a = numbers[70]
    b = numbers[98]
    sum = 0
    for i in range(a + 1, b):
        if i not in numbers:
            sum += i
    if sum % 2 == 1:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:]