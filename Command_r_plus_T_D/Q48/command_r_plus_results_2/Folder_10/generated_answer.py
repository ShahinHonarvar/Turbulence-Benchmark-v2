def return_binary_or_hexa(numbers: tuple[int, ...]) -> str:
    a, b = (numbers[36], numbers[54])
    range_sum = 0
    for i in range(a + 1, b):
        if i not in numbers[36:55]:
            range_sum += i
    if range_sum:
        return bin(range_sum)[2:] if range_sum % 2 else hex(range_sum)[2:].upper()
    return ''