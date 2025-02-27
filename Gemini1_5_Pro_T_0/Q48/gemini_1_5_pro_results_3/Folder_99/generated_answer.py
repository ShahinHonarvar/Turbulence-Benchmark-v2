def return_binary_or_hexa(numbers):
    a = numbers[427]
    b = numbers[669]
    sum_of_missing_numbers = 0
    for i in range(a + 1, b):
        if i not in numbers[427:669]:
            sum_of_missing_numbers += i
    if sum_of_missing_numbers == 0:
        return ''
    if sum_of_missing_numbers % 2:
        return bin(sum_of_missing_numbers)[2:]
    else:
        return hex(sum_of_missing_numbers)[2:]