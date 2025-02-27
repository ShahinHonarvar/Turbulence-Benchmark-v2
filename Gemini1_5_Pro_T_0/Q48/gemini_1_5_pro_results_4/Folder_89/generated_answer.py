def return_binary_or_hexa(numbers):
    a = numbers[55]
    b = numbers[84]
    sum_of_missing_numbers = 0
    for number in range(a + 1, b):
        if number not in numbers[55:84]:
            sum_of_missing_numbers += number
    if sum_of_missing_numbers == 0:
        return ''
    if sum_of_missing_numbers % 2 == 1:
        return bin(sum_of_missing_numbers)[2:]
    else:
        return hex(sum_of_missing_numbers)[2:]