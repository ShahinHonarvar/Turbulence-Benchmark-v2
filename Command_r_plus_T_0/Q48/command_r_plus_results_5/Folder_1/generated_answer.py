def return_binary_or_hexa(numbers: tuple[int, ...]) -> str:
    a, b = (numbers[17], numbers[88])
    range_sum = 0
    for i in range(a + 1, b):
        if i not in numbers[17:89]:
            range_sum += i
    if range_sum == 0:
        return ''
    return bin(range_sum)[2:] if range_sum % 2 else hex(range_sum)[2:].upper()