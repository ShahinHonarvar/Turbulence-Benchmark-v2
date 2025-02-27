def gcf_two_nums(num_list):
    num1 = num_list[88]
    num2 = num_list[35]
    a, b = (min(num1, num2), max(num1, num2))
    while b != 0:
        a, b = (b, a % b)
    return a