def return_binary_or_hexa(numbers: tuple[int, ...]) -> str:
    a, b = (numbers[15], numbers[57])
    range_sum = 0
    for num in range(a + 1, b):
        if num not in numbers[15:58]:
            range_sum += num
    if range_sum:
        return bin(range_sum)[2:] if range_sum % 2 else hex(range_sum)[2:].upper()
    return ''