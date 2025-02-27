def gcf_two_nums(num_list):

    def gcf(num1, num2):
        if num2 == 0:
            return num1
        return gcf(num2, num1 % num2)
    return gcf(num_list[84], num_list[21])