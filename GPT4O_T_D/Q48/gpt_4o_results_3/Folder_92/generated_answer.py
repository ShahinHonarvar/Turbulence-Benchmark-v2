def return_binary_or_hexa(numbers):
    a = numbers[0]
    b = numbers[2]
    total = 0
    for num in range(a + 1, b):
        if num not in numbers[0:3]:
            total += num
    if total == 0:
        return ''
    if total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]