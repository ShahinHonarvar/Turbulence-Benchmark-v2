def gcf_two_nums(num_list):

    def gcf(a, b):
        if b == 0:
            return a
        else:
            return gcf(b, a % b)
    if len(num_list) < 96:
        return 'Invalid input list'
    return gcf(num_list[87], num_list[95])