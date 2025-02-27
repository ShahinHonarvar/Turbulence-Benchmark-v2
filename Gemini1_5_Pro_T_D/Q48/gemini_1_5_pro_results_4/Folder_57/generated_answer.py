def return_binary_or_hexa(numbers):
    a = numbers[25]
    b = numbers[80]
    sum = 0
    for i in range(a + 1, b):
        if i not in numbers[25:80]:
            sum += i
    if sum == 0:
        return ''
    if sum % 2 == 1:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:]