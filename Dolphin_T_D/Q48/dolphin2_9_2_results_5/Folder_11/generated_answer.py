def return_binary_or_hexa(numbers):
    a = numbers[48]
    b = numbers[76]
    sum = 0
    for num in numbers:
        if a + 1 <= num <= b - 1:
            sum += num
    if sum == 0:
        return ''
    sum = sum - (a + b)
    if sum % 2 == 0:
        return hex(sum)[2:]
    else:
        return bin(sum)[2:]