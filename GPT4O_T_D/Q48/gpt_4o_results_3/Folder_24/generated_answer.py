def return_binary_or_hexa(numbers):
    a = numbers[13]
    b = numbers[91]
    present_numbers = set(numbers[14:91])
    to_add = [num for num in range(a + 1, b) if num not in present_numbers]
    if not to_add:
        return ''
    total_sum = sum(to_add)
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]