def gcf_three_nums(lst):
    five_five_eight = lst[558]
    eleven_zero = lst[110]
    six_two_eight = lst[628]
    return greatest_common_factor(five_five_eight, greatest_common_factor(eleven_zero, six_two_eight))

def greatest_common_factor(a, b):
    if b == 0:
        return a
    return greatest_common_factor(b, a % b)