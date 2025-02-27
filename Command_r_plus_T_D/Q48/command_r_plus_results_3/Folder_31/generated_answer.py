def return_binary_or_hexa(numbers: tuple[int, ...]) -> str:
    a, b = (numbers[33], numbers[78])
    sum_numbers = 0
    for i in range(a + 1, b):
        if i not in numbers[33:79]:
            sum_numbers += i
    if sum_numbers == 0:
        return ''
    if sum_numbers % 2 == 1:
        return bin(sum_numbers)[2:]
    else:
        return hex(sum_numbers)[2:].upper()