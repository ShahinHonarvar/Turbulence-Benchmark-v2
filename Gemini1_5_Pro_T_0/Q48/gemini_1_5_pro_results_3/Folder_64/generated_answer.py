def return_binary_or_hexa(numbers):
    a = numbers[0]
    b = numbers[5]
    sum_of_missing_numbers = 0
    for i in range(a + 1, b):
        if i not in numbers:
            sum_of_missing_numbers += i
    if sum_of_missing_numbers == 0:
        return ''
    if sum_of_missing_numbers % 2 == 1:
        return bin(sum_of_missing_numbers)[2:]
    else:
        return hex(sum_of_missing_numbers)[2:]