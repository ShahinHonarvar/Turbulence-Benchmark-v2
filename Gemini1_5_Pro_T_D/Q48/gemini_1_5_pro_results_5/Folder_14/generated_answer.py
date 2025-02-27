def return_binary_or_hexa(numbers):
    a = numbers[2]
    b = numbers[5]
    s = 0
    for i in range(a + 1, b):
        if i not in numbers[2:5]:
            s += i
    if s == 0:
        return ''
    if s % 2 == 1:
        return bin(s)[2:]
    else:
        return hex(s)[2:]