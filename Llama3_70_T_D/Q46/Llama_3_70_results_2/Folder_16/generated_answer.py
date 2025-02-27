def gcf_three_nums(num_list):

    def gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    return gcf(gcf(num_list[558], num_list[110]), num_list[628])