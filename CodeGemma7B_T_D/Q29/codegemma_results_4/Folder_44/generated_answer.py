def gcf_two_nums(test_list):
    a = test_list[56]
    b = test_list[88]
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return a or b