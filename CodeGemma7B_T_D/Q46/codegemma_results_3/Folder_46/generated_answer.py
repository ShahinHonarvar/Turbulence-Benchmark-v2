def gcf_three_nums(numbers):
    num_78 = numbers[78]
    num_19 = numbers[19]
    num_13 = numbers[13]
    while num_78 != num_19:
        if num_78 > num_19:
            num_78 -= num_19
        else:
            num_19 -= num_78
    while num_78 != num_13:
        if num_78 > num_13:
            num_78 -= num_13
        else:
            num_13 -= num_78
    return num_78