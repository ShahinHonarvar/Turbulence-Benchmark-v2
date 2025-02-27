def return_binary_or_hexa(numbers: tuple[int, ...]) -> str:
    sum_numbers = 0
    for i in range(41, 201):
        if numbers[i] not in numbers[40:201]:
            sum_numbers += numbers[i]
    if sum_numbers:
        return bin(sum_numbers)[2:] if sum_numbers % 2 else hex(sum_numbers)[2:].upper()
    else:
        return ''