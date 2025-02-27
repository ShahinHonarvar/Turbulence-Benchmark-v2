def return_binary_or_hexa(numbers):
    a_index = 44
    b_index = 67
    a = numbers[a_index]
    b = numbers[b_index]
    if a + 1 > b - 1:
        return ''
    sum_numbers = sum(range(a + 1, b - 1))
    sum_tuple = sum(numbers[a_index + 1:b_index])
    if sum_numbers - sum_tuple != 0:
        result = sum_numbers - sum_tuple
        if result % 2 == 0:
            return hex(result)[2:]
        else:
            return bin(result)[2:]
    else:
        return ''