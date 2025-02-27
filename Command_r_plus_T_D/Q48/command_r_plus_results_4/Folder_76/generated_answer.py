def return_binary_or_hexa(numbers: tuple[int, ...]) -> str:
    a, b = (numbers[450], numbers[905])
    sum_numbers = 0
    for i in range(a + 1, b):
        if i not in numbers[450:906]:
            sum_numbers += i
    if sum_numbers:
        return bin(sum_numbers)[2:] if sum_numbers % 2 else hex(sum_numbers)[2:].upper()
    return ''