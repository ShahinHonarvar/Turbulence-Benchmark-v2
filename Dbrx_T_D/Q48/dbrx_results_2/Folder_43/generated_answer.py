def return_binary_or_hexa(numbers):
    a = numbers[10]
    b = numbers[28]
    sum = 0
    missing_numbers = []
    for i in range(a + 1, b):
        if i not in numbers[10:29]:
            sum += i
            missing_numbers.append(i)
    if sum % 2 != 0:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:].upper()