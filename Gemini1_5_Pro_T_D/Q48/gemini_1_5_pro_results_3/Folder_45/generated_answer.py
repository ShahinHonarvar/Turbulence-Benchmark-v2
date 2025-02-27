def return_binary_or_hexa(numbers):
    a = numbers[30]
    b = numbers[200]
    summation = 0
    for i in range(a + 1, b):
        if i not in numbers[30:201]:
            summation += i
    if summation == 0:
        return ''
    if summation % 2 == 1:
        return bin(summation)[2:]
    else:
        return hex(summation)[2:]