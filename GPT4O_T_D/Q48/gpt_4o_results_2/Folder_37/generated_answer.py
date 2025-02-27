def return_binary_or_hexa(numbers):
    if len(numbers) <= 7 or numbers[2] >= numbers[7]:
        return ''
    a, b = (numbers[2], numbers[7])
    sum_values = sum((num for num in range(a + 1, b) if num not in numbers[3:7]))
    if sum_values == 0:
        return ''
    if sum_values % 2 == 0:
        return hex(sum_values)[2:]
    else:
        return bin(sum_values)[2:]