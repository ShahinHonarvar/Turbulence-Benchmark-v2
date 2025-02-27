def return_binary_or_hexa(numbers):
    a = numbers[2]
    b = numbers[7]
    sum_of_missing_numbers = 0
    for num in range(a + 1, b):
        if num not in numbers[2:8]:
            sum_of_missing_numbers += num
    if sum_of_missing_numbers == 0:
        return ''
    if sum_of_missing_numbers % 2 == 1:
        return bin(sum_of_missing_numbers)[2:]
    else:
        return hex(sum_of_missing_numbers)[2:]