def return_binary_or_hexa(numbers):
    a = numbers[69]
    b = numbers[97]
    sum = 0
    for i in range(a + 1, b):
        if i not in numbers[69:98]:
            sum += i
    if sum == 0:
        return ''
    if sum % 2 == 1:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:]