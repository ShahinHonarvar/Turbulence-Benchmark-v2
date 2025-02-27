def return_binary_or_hexa(numbers):
    a, b = (numbers[56], numbers[88])
    sub_range = set(range(a + 1, b))
    missing_numbers = sub_range.difference(set(numbers[56 + 1:88]))
    missing_sum = sum(missing_numbers)
    if missing_sum == 0:
        return ''
    elif missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]