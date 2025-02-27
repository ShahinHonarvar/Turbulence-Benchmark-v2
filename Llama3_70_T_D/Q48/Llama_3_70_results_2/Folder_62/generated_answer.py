def return_binary_or_hexa(numbers):
    a = numbers[50]
    b = numbers[92]
    total_sum = sum((i for i in range(a + 1, b) if i not in numbers[51:93]))
    return bin(total_sum)[2:] if total_sum % 2 != 0 else hex(total_sum)[2:]