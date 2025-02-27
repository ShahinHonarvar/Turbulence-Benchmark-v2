def return_binary_or_hexa(numbers):
    if len(numbers) <= 80:
        return ''
    a, b = (numbers[25], numbers[80])
    if a + 1 >= b:
        return ''
    summed_values = sum((i for i in range(a + 1, b) if i not in numbers[26:81]))
    if summed_values % 2 != 0:
        return bin(summed_values)[2:]
    else:
        return hex(summed_values)[2:]