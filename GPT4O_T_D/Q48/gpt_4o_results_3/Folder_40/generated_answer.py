def return_binary_or_hexa(numbers):
    a = numbers[0]
    b = numbers[3]
    total_sum = sum((x for x in range(a + 1, b) if x not in numbers[:4]))
    if total_sum == 0:
        return ''
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]