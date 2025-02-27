def return_binary_or_hexa(numbers):
    result = 0
    for i in range(numbers[200] + 1, numbers[202]):
        if i not in numbers[200:202]:
            result += i
    if result % 2 == 0:
        return hex(result)[2:].upper()
    else:
        return bin(result)[2:]