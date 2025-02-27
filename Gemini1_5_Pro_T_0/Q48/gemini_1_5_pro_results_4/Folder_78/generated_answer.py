def return_binary_or_hexa(numbers):
    a = numbers[62]
    b = numbers[96]
    sum = 0
    for i in range(a + 1, b):
        if i not in numbers[62:97]:
            sum += i
    if sum == 0:
        return ''
    if sum % 2 == 1:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:]