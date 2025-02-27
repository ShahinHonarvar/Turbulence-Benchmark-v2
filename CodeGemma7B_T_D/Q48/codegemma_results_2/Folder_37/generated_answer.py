def return_binary_or_hexa(numbers):
    a = numbers[2]
    b = numbers[7]
    truncated_nums = numbers[2:7]
    result = sum((i for i in range(a + 1, b) if i not in truncated_nums))
    return bin(result)[2:] if result % 2 else hex(result)[2:].upper() if result % 2 else ''