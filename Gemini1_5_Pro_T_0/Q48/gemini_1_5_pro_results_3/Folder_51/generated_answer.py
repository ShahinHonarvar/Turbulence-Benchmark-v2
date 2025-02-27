def return_binary_or_hexa(numbers):
    a = numbers[6]
    b = numbers[9]
    sum_of_missing_numbers = 0
    for i in range(a + 1, b):
        if i not in numbers[6:10]:
            sum_of_missing_numbers += i
    if sum_of_missing_numbers == 0:
        return ''
    if sum_of_missing_numbers % 2 == 1:
        return bin(sum_of_missing_numbers)[2:]
    else:
        return hex(sum_of_missing_numbers)[2:]