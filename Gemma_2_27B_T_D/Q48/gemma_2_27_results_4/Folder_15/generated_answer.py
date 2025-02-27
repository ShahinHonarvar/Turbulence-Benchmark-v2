def return_binary_or_hexa(numbers):
    a = numbers[0]
    b = numbers[4]
    sum = 0
    for i in range(a + 1, b):
        if i not in numbers:
            sum += i
    if sum % 2 != 0:
        return bin(sum)[2:]
    elif sum == 0:
        return ''
    else:
        return hex(sum)[2:]