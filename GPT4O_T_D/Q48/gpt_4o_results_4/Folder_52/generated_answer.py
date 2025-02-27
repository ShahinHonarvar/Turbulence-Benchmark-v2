def return_binary_or_hexa(numbers):
    a = numbers[38]
    b = numbers[81]
    numbers_set = set(numbers[39:81])
    total_sum = sum((x for x in range(a + 1, b) if x not in numbers_set))
    if total_sum == 0:
        return ''
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]