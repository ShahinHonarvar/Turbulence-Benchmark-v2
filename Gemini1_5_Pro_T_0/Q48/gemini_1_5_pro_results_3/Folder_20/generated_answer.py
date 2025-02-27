def return_binary_or_hexa(numbers):
    a = numbers[27]
    b = numbers[96]
    sum = 0
    for i in range(a + 1, b):
        if i not in numbers[27:96]:
            sum += i
    if sum == 0:
        return ''
    if sum % 2 == 1:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:]