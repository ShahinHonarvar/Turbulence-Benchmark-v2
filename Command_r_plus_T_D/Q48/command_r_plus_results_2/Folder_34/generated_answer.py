def return_binary_or_hexa(numbers: tuple[int, ...]) -> str:
    a, b = (numbers[60], numbers[200])
    sum_numbers = sum((i for i in range(a + 1, b) if i not in numbers[60:201]))
    if sum_numbers in numbers[60:201]:
        return ''
    return bin(sum_numbers)[2:] if sum_numbers % 2 else hex(sum_numbers)[2:].upper()