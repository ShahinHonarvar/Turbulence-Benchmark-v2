def return_binary_or_hexa(numbers):
    a = numbers[20]
    b = numbers[51]
    sum_of_missing_numbers = 0
    for i in range(a + 1, b):
        if i not in numbers[20:52]:
            sum_of_missing_numbers += i
    if sum_of_missing_numbers == 0:
        return ''
    elif sum_of_missing_numbers % 2 == 1:
        return bin(sum_of_missing_numbers)[2:]
    else:
        return hex(sum_of_missing_numbers)[2:].upper()