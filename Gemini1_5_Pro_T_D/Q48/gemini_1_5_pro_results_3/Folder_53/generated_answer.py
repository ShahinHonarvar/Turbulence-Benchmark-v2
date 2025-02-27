def return_binary_or_hexa(numbers):
    a = numbers[200]
    b = numbers[202]
    sum = 0
    for i in range(a + 1, b):
        if i not in numbers[201:202]:
            sum += i
    if sum == 0:
        return ''
    elif sum % 2 == 1:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:]