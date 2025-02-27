def return_binary_or_hexa(numbers: tuple[int, ...]) -> str:
    a, b = (numbers[62], numbers[96])
    range_sum = 0
    for i in range(a + 1, b):
        if i not in numbers[62:97]:
            range_sum += i
    if range_sum == 0:
        return ''
    return hex(range_sum)[2:].upper() if range_sum % 2 == 0 else bin(range_sum)[2:]