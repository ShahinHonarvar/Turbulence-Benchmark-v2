def return_binary_or_hexa(numbers):
    a = numbers[60]
    b = numbers[200]
    sum = 0
    for i in range(a + 1, b):
        if i not in numbers[61:200]:
            sum += i
    if sum == 0:
        return ''
    if sum % 2 == 1:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:]