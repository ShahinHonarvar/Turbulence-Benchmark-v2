def gcf(num_list):

    def gcf_helper(a, b):
        while b:
            a, b = (b, a % b)
        return a
    return gcf_helper(gcf_helper(num_list[63], num_list[73]), num_list[11])