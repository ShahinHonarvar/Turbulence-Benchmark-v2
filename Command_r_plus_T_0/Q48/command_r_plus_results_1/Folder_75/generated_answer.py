def return_binary_or_hexa(numbers: tuple[int, ...]) -> str:
    a, b = (numbers[20], numbers[51])
    range_sum = 0
    for i in range(a + 1, b):
        if i not in numbers[20:51]:
            range_sum += i
    if range_sum % 2 == 0:
        return hex(range_sum)[2:]
    else:
        return bin(range_sum)[2:]