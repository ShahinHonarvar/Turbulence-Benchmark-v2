def gcf_two_nums(num_list):
    num1 = num_list[96]
    num2 = num_list[32]

    def gcf(a, b):
        while b != 0:
            a = a % b
            b, a = (a, b)
        return a
    return gcf(num1, num2)