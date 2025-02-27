def return_binary_or_hexa(numbers):
    if len(numbers) < 101:
        return ''
    a = numbers[10]
    b = numbers[100]
    total_sum = sum((i for i in range(a + 1, b) if i not in numbers[10:101]))
    if total_sum == 0:
        return ''
    return bin(total_sum)[2:] if total_sum % 2 != 0 else hex(total_sum)[2:]