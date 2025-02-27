def gcf_three_nums(num_list):

    def gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    gcf_36_54 = gcf(num_list[36], num_list[54])
    return gcf(gcf_36_54, num_list[85])