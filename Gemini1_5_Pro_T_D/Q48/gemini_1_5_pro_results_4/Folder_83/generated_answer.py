def return_binary_or_hexa(numbers):
    a = numbers[90]
    b = numbers[200]
    sum = 0
    for i in range(a + 1, b):
        if i not in numbers[90:201]:
            sum += i
    if sum == 0:
        return ''
    if sum % 2 == 1:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:]