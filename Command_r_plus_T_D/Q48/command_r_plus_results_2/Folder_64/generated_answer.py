def return_binary_or_hexa(numbers: tuple[int, ...]) -> str:
    a, b = (numbers[0], numbers[5])
    sum_numbers = sum(range(a + 1, b))
    for num in range(a + 1, b):
        if num in numbers[1:6]:
            sum_numbers -= num
    if sum_numbers == 0:
        return ''
    if sum_numbers % 2 == 1:
        return bin(sum_numbers)[2:]
    else:
        return hex(sum_numbers)[2:].upper()