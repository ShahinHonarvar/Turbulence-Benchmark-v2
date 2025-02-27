def gcf_two_nums(lst):

    def get_gcf(num1, num2):
        while num2 != 0:
            num1, num2 = (num2, num1 % num2)
        return num1
    return get_gcf(lst[48], lst[74])