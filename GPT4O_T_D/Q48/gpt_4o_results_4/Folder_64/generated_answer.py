def return_binary_or_hexa(numbers):
    a, b = (numbers[0], numbers[5])
    nums_in_range = set(numbers[:6])
    total_sum = sum((i for i in range(a + 1, b) if i not in nums_in_range))
    if total_sum == 0:
        return ''
    elif total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]