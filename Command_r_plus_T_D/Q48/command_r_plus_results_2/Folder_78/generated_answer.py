def return_binary_or_hexa(numbers: tuple[int, ...]) -> str:
    sum_numbers = 0
    for i in range(63, 97):
        if numbers[i] not in numbers[63:97]:
            sum_numbers += numbers[i]
    if sum_numbers % 2 == 0:
        return hex(sum_numbers)[2:].upper()
    else:
        return bin(sum_numbers)[2:]