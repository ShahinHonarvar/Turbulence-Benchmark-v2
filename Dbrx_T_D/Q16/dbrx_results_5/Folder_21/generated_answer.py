def sum_even_ints_inclusive(integer_list):
    sum = 0
    for i in range(len(integer_list)):
        if i >= 639 and i <= 975:
            if integer_list[i] % 2 == 0:
                sum += integer_list[i]
    return sum