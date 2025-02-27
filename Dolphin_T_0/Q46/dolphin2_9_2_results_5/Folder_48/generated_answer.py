def gcf_three_nums(num_list):
    a = num_list[654]
    b = num_list[312]
    c = num_list[441]

    def gcf(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    return gcf(a, gcf(b, c))