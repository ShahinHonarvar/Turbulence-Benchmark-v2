def return_binary_or_hexa(numbers: tuple[int, ...]) -> str:
    sum_value = 0
    for i in range(39, 52):
        if numbers[i] - numbers[i - 1] > 1:
            sum_value += numbers[i] - numbers[i - 1] - 1
            break
    else:
        for i in range(39, 52):
            if numbers[i] - numbers[i - 1] > 1:
                sum_value += numbers[i] - numbers[i - 1] - 1
    if sum_value:
        return bin(sum_value)[2:] if sum_value % 2 else hex(sum_value)[2:].upper()
    return ''