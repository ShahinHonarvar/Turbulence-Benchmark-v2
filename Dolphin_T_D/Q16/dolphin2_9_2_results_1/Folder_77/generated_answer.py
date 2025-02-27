def sum_even_ints_inclusive(n_list):
    sum_ = 0
    specified_range = n_list[527:539]
    for int_ in specified_range:
        if int_ % 2 == 0:
            sum_ += int_
    if sum_ == 0:
        return 0
    else:
        return sum_