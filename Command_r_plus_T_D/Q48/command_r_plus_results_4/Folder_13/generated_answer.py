def return_binary_or_hexa(numbers: tuple[int, ...]) -> str:
    a, b = (numbers[46], numbers[91])
    range_sum = 0
    range_set = set(numbers[46:92])
    for i in range(a + 1, b):
        if i not in range_set:
            range_sum += i
    if range_sum == 0:
        return ''
    return hex(range_sum)[2:].upper() if range_sum % 2 == 0 else bin(range_sum)[2:]