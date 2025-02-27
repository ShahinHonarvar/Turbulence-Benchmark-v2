def sum_even_ints_inclusive(num_list):
    result = 0
    for i in range(0, 11):
        if i >= 0 and i <= 10 and (num_list[i] % 2 == 0):
            result += num_list[i]
        if i > 10:
            return result