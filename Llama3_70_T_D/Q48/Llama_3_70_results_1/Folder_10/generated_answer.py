def return_binary_or_hexa(numbers):
    a = numbers[36]
    b = numbers[54]
    numbers_in_range = set(numbers[36:55])
    missing_sum = sum((i for i in range(a + 1, b) if i not in numbers_in_range))
    if missing_sum == 0:
        return ''
    elif missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]