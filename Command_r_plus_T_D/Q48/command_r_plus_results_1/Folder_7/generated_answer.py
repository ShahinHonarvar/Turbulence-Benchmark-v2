def return_binary_or_hexa(numbers: tuple[int, ...]) -> str:
    sum_numbers = 0
    range_numbers = set(numbers[10:98])
    for i in range(numbers[10] + 1, numbers[97]):
        if i not in range_numbers:
            sum_numbers += i
    if sum_numbers:
        return bin(sum_numbers)[2:] if sum_numbers % 2 else hex(sum_numbers)[2:].upper()
    else:
        return ''