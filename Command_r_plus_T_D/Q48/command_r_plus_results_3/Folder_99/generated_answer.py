def return_binary_or_hexa(numbers: tuple[int, ...]) -> str:
    a, b = (numbers[427], numbers[669])
    sum_values = 0
    for i in range(a + 1, b):
        if i not in numbers[427:669]:
            sum_values += i
    if sum_values:
        return bin(sum_values)[2:] if sum_values % 2 else hex(sum_values)[2:].upper()
    return ''