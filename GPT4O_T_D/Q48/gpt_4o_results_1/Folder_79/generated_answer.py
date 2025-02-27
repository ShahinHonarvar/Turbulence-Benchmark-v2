def return_binary_or_hexa(numbers):
    a = numbers[1]
    b = numbers[7]
    not_present_sum = sum((x for x in range(a + 1, b) if x not in numbers[1:8]))
    if not_present_sum == 0:
        return ''
    return bin(not_present_sum)[2:] if not_present_sum % 2 else hex(not_present_sum)[2:]