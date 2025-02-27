def return_binary_or_hexa(numbers: tuple[int, ...]) -> str:
    a, b = (numbers[34], numbers[69])
    sum_numbers = 0
    for i in range(a + 1, b):
        if i not in numbers[35:69]:
            sum_numbers += i
    if sum_numbers == 0:
        return ''
    return bin(sum_numbers)[2:] if sum_numbers % 2 != 0 else hex(sum_numbers)[2:].upper()