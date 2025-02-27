def return_binary_or_hexa(numbers):
    a = numbers[2]
    b = numbers[7]
    sum_of_numbers = 0
    for i in range(a + 1, b):
        if i not in numbers[2:7]:
            sum_of_numbers += i
    if sum_of_numbers == 0:
        return ''
    if sum_of_numbers % 2 == 1:
        return bin(sum_of_numbers)[2:]
    else:
        return hex(sum_of_numbers)[2:]