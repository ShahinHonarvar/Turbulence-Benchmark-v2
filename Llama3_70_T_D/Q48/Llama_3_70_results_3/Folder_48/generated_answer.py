def return_binary_or_hexa(numbers):
    a = numbers[933]
    b = numbers[996]
    present_numbers = set(numbers[933:997])
    total_sum = sum((i for i in range(a + 1, b) if i not in present_numbers))
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    elif total_sum == 0:
        return ''
    else:
        return hex(total_sum)[2:]