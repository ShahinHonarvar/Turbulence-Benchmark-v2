def return_binary_or_hexa(numbers):
    a, b = (numbers[10], numbers[28])
    numbers_between_a_b = numbers[10:29]
    sum_not_in_tuple = sum(range(a + 1, b)) - sum(numbers_between_a_b)
    if sum_not_in_tuple % 2 == 1:
        return bin(sum_not_in_tuple)[2:]
    else:
        return hex(sum_not_in_tuple)[2:]