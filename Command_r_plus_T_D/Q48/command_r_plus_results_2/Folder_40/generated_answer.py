def return_binary_or_hexa(numbers: tuple[int, ...]) -> str:
    a, b = (numbers[0], numbers[3])
    sum_numbers = sum(range(a + 1, b))
    for num in numbers[1:3]:
        if a < num < b:
            sum_numbers -= num
    if sum_numbers:
        return bin(sum_numbers)[2:] if sum_numbers % 2 else hex(sum_numbers)[2:].upper()
    else:
        return ''