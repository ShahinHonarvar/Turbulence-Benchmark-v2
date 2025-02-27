def return_binary_or_hexa(numbers):
    a = numbers[36]
    b = numbers[85]
    sum_not_present = 0
    for i in range(a + 1, b):
        if i not in numbers[36:86]:
            sum_not_present += i
    if sum_not_present % 2:
        return bin(sum_not_present)[2:]
    else:
        return hex(sum_not_present)[2:].upper()