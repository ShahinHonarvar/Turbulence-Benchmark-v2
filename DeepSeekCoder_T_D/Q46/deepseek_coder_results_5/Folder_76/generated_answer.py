def gcf_three_nums(num_list):

    def gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    return gcf(num_list[876], gcf(num_list[203], num_list[100]))