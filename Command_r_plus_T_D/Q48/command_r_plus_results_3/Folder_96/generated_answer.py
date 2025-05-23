def return_binary_or_hexa(numbers: tuple[int, ...]) -> str:
    a, b = (numbers[50], numbers[200])
    sum_val = 0
    for i in range(a + 1, b):
        if i not in numbers[50:201]:
            sum_val += i
    if sum_val:
        return bin(sum_val)[2:] if sum_val % 2 else hex(sum_val)[2:].upper()
    return ''