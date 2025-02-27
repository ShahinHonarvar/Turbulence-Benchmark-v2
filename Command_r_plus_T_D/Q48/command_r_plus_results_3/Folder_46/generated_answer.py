def return_binary_or_hexa(numbers: tuple[int, ...]) -> str:
    a, b = (numbers[10], numbers[79])
    sum_range = sum(range(a + 1, b))
    for num in range(a + 1, b):
        if num in numbers[11:80]:
            sum_range -= num
    if sum_range == 0:
        return ''
    elif sum_range % 2 == 1:
        return bin(sum_range)[2:]
    else:
        return hex(sum_range)[2:].upper()