def return_binary_or_hexa(numbers):
    a, b = (numbers[45], numbers[48])
    total_sum = sum((i for i in range(a + 1, b) if i not in numbers[45:49]))
    if not total_sum:
        return ''
    elif total_sum % 2:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]