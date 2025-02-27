def return_binary_or_hexa(numbers: tuple[int, ...]) -> str:
    a, b = (numbers[49], numbers[74])
    range_sum = 0
    for num in range(a + 1, b):
        if num not in numbers[50:74]:
            range_sum += num
    if range_sum == 0:
        return ''
    return bin(range_sum)[2:] if range_sum % 2 != 0 else hex(range_sum)[2:].upper()