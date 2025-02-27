def return_binary_or_hexa(test_list):

    def f(a, b, num_list):
        if not num_list:
            return 0
        if len(num_list) % 2 == 1:
            return 0
        sum_var = 0
        for i in range(len(num_list)):
            num = num_list[i]
            if num >= a and num <= b:
                sum_var += num
        if sum_var % 2 == 1:
            return format(sum_var, 'b')
        return format(sum_var, 'x')
    return f(20, 93, test_list)