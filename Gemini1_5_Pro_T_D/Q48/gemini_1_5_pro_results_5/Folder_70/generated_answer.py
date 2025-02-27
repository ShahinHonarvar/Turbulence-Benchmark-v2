def return_binary_or_hexa(numbers):
    a = numbers[43]
    b = numbers[70]
    sum = 0
    for i in range(a + 1, b):
        if i not in numbers[43:71]:
            sum += i
    if sum % 2 == 1:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:].upper()