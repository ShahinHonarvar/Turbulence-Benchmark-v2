def return_binary_or_hexa(numbers):
    a = numbers[32]
    b = numbers[99]
    sum = 0
    for i in range(a + 1, b):
        if i not in numbers[32:99]:
            sum += i
    if sum == 0:
        return ''
    elif sum % 2 == 0:
        return hex(sum)[2:].lstrip('0')
    else:
        return bin(sum)[2:].lstrip('0')