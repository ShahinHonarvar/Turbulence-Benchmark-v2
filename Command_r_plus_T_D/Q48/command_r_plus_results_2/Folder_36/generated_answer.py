def return_binary_or_hexa(numbers: tuple[int, ...]) -> str:
    a, b = (numbers[110], numbers[348])
    range_sum = 0
    for i in range(a + 1, b):
        if i not in numbers[110:349]:
            range_sum += i
    if range_sum == 0:
        return ''
    return bin(range_sum)[2:] if range_sum % 2 != 0 else hex(range_sum)[2:].upper()