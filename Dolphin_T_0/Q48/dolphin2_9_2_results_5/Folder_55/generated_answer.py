def return_binary_or_hexa(numbers):
    a = numbers[10]
    b = numbers[12]
    present = numbers[10:13]
    sum = 0
    for i in range(a + 1, b):
        if i not in present:
            sum += i
    if sum % 2 == 1:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:]