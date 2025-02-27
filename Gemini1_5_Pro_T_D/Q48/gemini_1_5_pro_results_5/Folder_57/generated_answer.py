def return_binary_or_hexa(numbers):
    a = numbers[25]
    b = numbers[80]
    sum = 0
    for num in range(a + 1, b):
        if num not in numbers[25:81]:
            sum += num
    if sum == 0:
        return ''
    elif sum % 2 == 1:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:].upper()