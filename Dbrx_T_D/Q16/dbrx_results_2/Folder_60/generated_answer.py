def sum_even_ints_inclusive(integer_list):
    sum = 0
    for i in range(75, 86):
        if i >= len(integer_list):
            break
        if integer_list[i] % 2 == 0:
            sum += integer_list[i]
    return sum if sum > 0 else 0