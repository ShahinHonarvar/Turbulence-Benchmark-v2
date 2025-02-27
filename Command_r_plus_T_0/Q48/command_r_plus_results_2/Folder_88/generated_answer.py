def return_binary_or_hexa(numbers: tuple[int, ...]) -> str:
    a, b = (numbers[3], numbers[9])
    range_sum = 0
    for num in range(a + 1, b):
        if num not in numbers[3:10]:
            range_sum += num
    if range_sum == 0:
        return ''
    return bin(range_sum)[2:] if range_sum % 2 else hex(range_sum)[2:].upper()