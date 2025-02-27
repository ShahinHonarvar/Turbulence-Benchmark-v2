def return_binary_or_hexa(numbers):
    a, b = (numbers[50], numbers[92])
    sum_of_missing_numbers = 0
    for num in range(a + 1, b):
        if num not in numbers[50:93]:
            sum_of_missing_numbers += num
    if sum_of_missing_numbers % 2 == 0:
        return hex(sum_of_missing_numbers)[2:].upper()
    else:
        return bin(sum_of_missing_numbers)[2:]