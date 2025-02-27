def return_binary_or_hexa(numbers: tuple[int, ...]) -> str:
    a = numbers[27]
    b = numbers[96]
    range_sum = 0
    for i in range(a + 1, b):
        if i not in numbers[28:96]:
            range_sum += i
    if range_sum == 0:
        return ''
    if range_sum % 2 == 1:
        return bin(range_sum)[2:]
    else:
        return hex(range_sum)[2:].upper()