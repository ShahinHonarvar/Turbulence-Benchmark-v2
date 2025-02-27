def return_binary_or_hexa(numbers):
    a = numbers[933]
    b = numbers[996]
    numbers_set = set(numbers[933:997])
    total = sum((i for i in range(a + 1, b) if i not in numbers_set))
    if total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]