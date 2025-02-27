def return_binary_or_hexa(numbers: tuple[int, ...]) -> str:
    a, b = (numbers[0], numbers[10])
    sum_of_missing_numbers = 0
    for i in range(a + 1, b):
        if i not in numbers:
            sum_of_missing_numbers += i
    if sum_of_missing_numbers % 2 == 0:
        return hex(sum_of_missing_numbers)[2:]
    else:
        return bin(sum_of_missing_numbers)[2:]