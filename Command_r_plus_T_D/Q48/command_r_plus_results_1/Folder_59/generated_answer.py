def return_binary_or_hexa(numbers: tuple[int, ...]) -> str:
    a, b = (numbers[0], numbers[10])
    sum_of_missing_numbers = sum(set(range(a + 1, b)) - set(numbers[:10]))
    if sum_of_missing_numbers in numbers[:10]:
        return ''
    return bin(sum_of_missing_numbers)[2:] if sum_of_missing_numbers % 2 else hex(sum_of_missing_numbers)[2:].upper()