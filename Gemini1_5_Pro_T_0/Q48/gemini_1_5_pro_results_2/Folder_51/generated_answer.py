def return_binary_or_hexa(numbers):
    a = numbers[6]
    b = numbers[9]
    sum = 0
    for num in range(a + 1, b):
        if num not in numbers[6:10]:
            sum += num
    if sum % 2 == 1:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:].upper()