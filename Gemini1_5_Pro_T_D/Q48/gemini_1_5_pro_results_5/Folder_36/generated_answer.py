def return_binary_or_hexa(numbers):
    a = numbers[110]
    b = numbers[348]
    total = 0
    for num in range(a + 1, b):
        if num not in numbers[110:349]:
            total += num
    if total == 0:
        return ''
    if total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]