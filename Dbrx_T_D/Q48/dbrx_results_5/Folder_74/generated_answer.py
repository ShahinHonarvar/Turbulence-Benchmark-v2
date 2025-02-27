def return_binary_or_hexa(numbers):
    a, b = (numbers[69], numbers[97])
    sum = 0
    for i in range(a + 1, b):
        if i not in numbers[69:98]:
            sum += i
    if sum % 2 != 0:
        return bin(sum)[2:].upper()
    else:
        return hex(sum)[2:].upper()