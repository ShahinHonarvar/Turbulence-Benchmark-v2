def return_binary_or_hexa(numbers):
    a, _, _, _, b = numbers
    total_sum = sum((i for i in range(a + 1, b) if i not in numbers[:5]))
    return bin(total_sum)[2:] if total_sum % 2 else hex(total_sum)[2:]