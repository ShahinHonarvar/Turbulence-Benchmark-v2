def return_binary_or_hexa(numbers: tuple[int, ...]) -> str:
    a, b = (numbers[44], numbers[78])
    range_sum = 0
    range_set = set(numbers[45:78])
    for num in range(a + 1, b):
        if num not in range_set:
            range_sum += num
    if range_sum == 0:
        return ''
    elif range_sum % 2 == 1:
        return bin(range_sum)[2:]
    else:
        return hex(range_sum)[2:].upper()