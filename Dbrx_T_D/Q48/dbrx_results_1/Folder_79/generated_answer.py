def return_binary_or_hexa(numbers):
    a, _, b = (numbers[1], 0, numbers[7])
    sum = 0
    for i in range(a + 1, b):
        if i not in numbers[1:7]:
            sum += i
    if sum % 2:
        return bin(sum).split('0b')[1]
    else:
        return hex(sum).split('0x')[1]