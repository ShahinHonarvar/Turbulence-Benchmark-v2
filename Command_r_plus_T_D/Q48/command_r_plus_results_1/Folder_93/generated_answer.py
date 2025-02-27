def return_binary_or_hexa(numbers: tuple[int, ...]) -> str:
    a, b = (numbers[57], numbers[85])
    sum_numbers = sum(range(a + 1, b))
    missing_numbers = [i for i in range(a + 1, b) if i not in numbers[58:85]]
    sum_missing_numbers = sum(missing_numbers)
    if sum_missing_numbers == 0:
        return ''
    if sum_missing_numbers % 2 == 1:
        return bin(sum_missing_numbers)[2:]
    else:
        return hex(sum_missing_numbers)[2:].upper()