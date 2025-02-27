def return_binary_or_hexa(numbers):
    a, b = (numbers[7], numbers[9])
    sum = 0
    for number in range(a + 1, b):
        if not number in numbers[7:9]:
            sum += number
    if sum % 2:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:].upper()