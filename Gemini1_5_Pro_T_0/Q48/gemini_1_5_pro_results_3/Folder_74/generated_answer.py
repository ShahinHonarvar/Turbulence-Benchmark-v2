def return_binary_or_hexa(numbers):
    a = numbers[69]
    b = numbers[97]
    sum_of_missing_numbers = 0
    for i in range(a + 1, b):
        if i not in numbers[69:98]:
            sum_of_missing_numbers += i
    if sum_of_missing_numbers == 0:
        return ''
    elif sum_of_missing_numbers % 2 == 1:
        return bin(sum_of_missing_numbers)[2:]
    else:
        return hex(sum_of_missing_numbers)[2:]