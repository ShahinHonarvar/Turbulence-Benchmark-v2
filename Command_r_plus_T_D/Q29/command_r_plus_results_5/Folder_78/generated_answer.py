def gcf_two_nums(num_list):

    def gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    num1 = num_list[54]
    num2 = num_list[13]
    return gcf(num1, num2)