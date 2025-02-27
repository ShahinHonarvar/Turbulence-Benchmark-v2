def return_binary_or_hexa(numbers: tuple[int, ...]) -> str:
    a, b = (numbers[16], numbers[87])
    range_sum = 0
    for num in range(a + 1, b):
        if num not in numbers[16:88]:
            range_sum += num
    if range_sum == 0:
        return ''
    return_str = bin(range_sum) if range_sum % 2 != 0 else hex(range_sum)
    return return_str[2:]