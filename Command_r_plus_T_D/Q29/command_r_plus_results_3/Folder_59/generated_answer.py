def gcf_two_nums(num_list):

    def gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    num1 = num_list[3]
    num2 = num_list[8]
    return gcf(num1, num2)