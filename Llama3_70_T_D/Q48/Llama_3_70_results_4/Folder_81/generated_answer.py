def return_binary_or_hexa(numbers):
    a = numbers[10]
    b = numbers[100]
    total_sum = sum((i for i in range(a + 1, b) if i not in numbers[10:101]))
    if total_sum % 2 == 0:
        return hex(total_sum)[2:]
    else:
        return bin(total_sum)[2:]