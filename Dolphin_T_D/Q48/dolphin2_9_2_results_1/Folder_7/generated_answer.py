def return_binary_or_hexa(numbers):
    a = numbers[10]
    b = numbers[97]
    if a > b:
        return ''
    sum_numbers = (a + 1 + b) * (b - a) // 2
    if all((numbers[i] == i + 1 for i in range(a, b + 1))):
        return ''
    if sum_numbers % 2:
        return bin(sum_numbers)[2:]
    else:
        return hex(sum_numbers)[2:]