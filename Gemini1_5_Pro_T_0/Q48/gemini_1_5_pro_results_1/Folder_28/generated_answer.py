def return_binary_or_hexa(numbers):
    a = numbers[86]
    b = numbers[99]
    total = 0
    for num in range(a + 1, b):
        if num not in numbers[86:100]:
            total += num
    if total == 0:
        return ''
    if total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]