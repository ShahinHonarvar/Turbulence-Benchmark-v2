def return_binary_or_hexa(numbers):
    a = numbers[10]
    b = numbers[100]
    sum_not_present = sum((i for i in range(a + 1, b) if i not in numbers[10:101]))
    if sum_not_present % 2:
        return bin(sum_not_present)[2:]
    else:
        return hex(sum_not_present)[2:].upper()