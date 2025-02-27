def return_binary_or_hexa(numbers):
    a = numbers[1]
    b = numbers[4]
    num_set = set(numbers[1:5])
    total_sum = sum((i for i in range(a + 1, b) if i not in num_set))
    if total_sum == 0:
        return ''
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]