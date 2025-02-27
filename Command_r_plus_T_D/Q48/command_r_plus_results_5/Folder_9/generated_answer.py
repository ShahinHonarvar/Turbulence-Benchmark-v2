def return_binary_or_hexa(numbers: tuple[int, ...]) -> str:
    a, b = (numbers[70], numbers[200])
    sum_numbers = 0
    for i in range(a + 1, b):
        if i not in numbers[70:201]:
            sum_numbers += i
    if sum_numbers:
        return bin(sum_numbers)[2:] if sum_numbers % 2 else hex(sum_numbers)[2:].upper()
    return ''