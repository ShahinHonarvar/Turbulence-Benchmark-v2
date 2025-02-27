def sum_odd_ints_inclusive(integer_list):
    start_index = 62
    end_index = 63
    sum = 0
    for i in range(start_index, end_index + 1):
        if i < 0 or i >= len(integer_list):
            return sum
        if integer_list[i] % 2 != 0:
            sum += integer_list[i]
    return sum