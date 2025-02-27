def return_binary_or_hexa(numbers):
    a = numbers[70]
    b = numbers[200]
    sum_of_missing_numbers = sum(set(range(a + 1, b)) - set(numbers[70:201]))
    if sum_of_missing_numbers % 2:
        return bin(sum_of_missing_numbers)[2:]
    else:
        return hex(sum_of_missing_numbers)