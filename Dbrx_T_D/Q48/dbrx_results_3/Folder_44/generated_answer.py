def return_binary_or_hexa(numbers):
    a = numbers[36]
    b = numbers[52]
    sum_of_numbers = sum((i for i in range(a + 1, b) if i not in numbers[36:53]))
    if sum_of_numbers % 2:
        return bin(sum_of_numbers)[2:]
    else:
        return hex(sum_of_numbers)[2:]