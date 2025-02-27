def return_binary_or_hexa(numbers: tuple[int, ...]) -> str:
    a, b = (numbers[90], numbers[200])
    sum_val = 0
    for i in range(a + 1, b):
        if i not in numbers[90:201]:
            sum_val += i
    if sum_val == 0:
        return ''
    return bin(sum_val)[2:] if sum_val % 2 != 0 else hex(sum_val)[2:].upper()