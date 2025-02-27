def return_binary_or_hexa(numbers):
    a = numbers[72]
    b = numbers[93]
    total_sum = sum((i for i in range(a + 1, b) if i not in numbers[72:94]))
    if not total_sum:
        return ''
    return bin(total_sum)[2:] if total_sum % 2 else hex(total_sum)[2:]