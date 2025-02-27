def return_binary_or_hexa(numbers):
    a = numbers[60]
    b = numbers[200]
    sum = 0
    for num in range(a + 1, b):
        if num not in numbers[60:201]:
            sum += num
    if sum % 2 != 0:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:]