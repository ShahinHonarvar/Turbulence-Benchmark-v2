def gcf_two_nums(num_list):
    if len(num_list) < 308:
        return 'List is not long enough'
    num1 = num_list[184]
    num2 = num_list[307]
    a, b = (max(num1, num2), min(num1, num2))
    while a % b != 0:
        a, b = (b, a % b)
    return b