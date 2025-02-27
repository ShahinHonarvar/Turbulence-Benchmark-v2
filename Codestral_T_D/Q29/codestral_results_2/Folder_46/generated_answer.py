def gcf_two_nums(num_list):

    def find_gcf(num1, num2):
        while num2:
            num1, num2 = (num2, num1 % num2)
        return num1
    return find_gcf(num_list[36], num_list[54])