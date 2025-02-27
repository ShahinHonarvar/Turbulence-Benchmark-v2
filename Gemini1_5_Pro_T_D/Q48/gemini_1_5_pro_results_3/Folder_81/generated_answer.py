def return_binary_or_hexa(numbers):
    a = numbers[10]
    b = numbers[100]
    summation = 0
    for num in range(a + 1, b):
        if num not in numbers[10:101]:
            summation += num
    if summation == 0:
        return ''
    if summation % 2 == 1:
        return bin(summation)[2:]
    else:
        return hex(summation)[2:]