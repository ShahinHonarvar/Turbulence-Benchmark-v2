def return_binary_or_hexa(numbers):
    a = numbers[69]
    b = numbers[97]
    sum = 0
    for num in range(a + 1, b):
        if num not in numbers[69:98]:
            sum += num
    if sum % 2 != 0:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:].upper()