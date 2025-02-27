def return_binary_or_hexa(numbers: tuple[int, ...]) -> str:
    a, b = (numbers[1], numbers[7])
    range_sum = 0
    for num in range(a + 1, b):
        if num not in numbers[1:8]:
            range_sum += num
    if range_sum:
        return bin(range_sum)[2:] if range_sum % 2 else hex(range_sum)[2:].upper()
    else:
        return ''