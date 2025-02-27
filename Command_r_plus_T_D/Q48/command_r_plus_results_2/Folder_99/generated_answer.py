def return_binary_or_hexa(numbers: tuple[int, ...]) -> str:
    sum_values = 0
    for i in range(428, 670):
        if numbers[i] not in numbers[427:669]:
            sum_values += numbers[i]
    if sum_values:
        return bin(sum_values)[2:] if sum_values % 2 else hex(sum_values)[2:].upper()
    else:
        return ''