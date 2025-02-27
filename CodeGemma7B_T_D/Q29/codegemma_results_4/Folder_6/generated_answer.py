def gcf_two_nums(list_of_ints):
    num_a = list_of_ints[25]
    num_b = list_of_ints[80]
    while num_a != num_b:
        if num_a > num_b:
            num_a -= num_b
        elif num_b > num_a:
            num_b -= num_a
    return num_a