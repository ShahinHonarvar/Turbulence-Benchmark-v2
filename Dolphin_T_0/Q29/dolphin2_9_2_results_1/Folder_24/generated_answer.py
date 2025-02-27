def gcf_two_nums(num_list):
    num1 = num_list[84]
    num2 = num_list[21]
    a, b = (max(num1, num2), min(num1, num2))
    while b != 0:
        a, b = (b, a % b)
    return a