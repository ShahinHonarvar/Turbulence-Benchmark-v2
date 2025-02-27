def sum_even_ints_inclusive(int_list):
    sum = 0
    for i in range(70, 201):
        if i % 2 == 0 and i < len(int_list):
            sum += int_list[i]
    return sum if sum > 0 else 0