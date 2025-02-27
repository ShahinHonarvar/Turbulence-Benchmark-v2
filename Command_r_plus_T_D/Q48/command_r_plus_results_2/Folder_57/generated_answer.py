def return_binary_or_hexa(numbers: tuple[int, ...]) -> str:
    a, b = (numbers[25], numbers[80])
    sum_val = 0
    for i in range(a + 1, b):
        if i not in numbers[26:80]:
            sum_val += i
    if sum_val == 0:
        return ''
    return bin(sum_val)[2:] if sum_val % 2 else hex(sum_val)[2:].upper()