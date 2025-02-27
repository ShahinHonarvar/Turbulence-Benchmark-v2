def return_binary_or_hexa(numbers: tuple[int, ...]) -> str:
    a, b = (numbers[1], numbers[8])
    sum_numbers = sum(range(a + 1, b))
    for i in range(2, 9):
        if a + 1 <= numbers[i] <= b - 1:
            sum_numbers -= numbers[i]
    if sum_numbers:
        return bin(sum_numbers)[2:] if sum_numbers % 2 else hex(sum_numbers)[2:].upper()
    return ''