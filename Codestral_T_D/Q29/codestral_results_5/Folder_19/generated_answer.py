def gcf_two_nums(num_list):

    def find_gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    return find_gcf(num_list[66], num_list[90])