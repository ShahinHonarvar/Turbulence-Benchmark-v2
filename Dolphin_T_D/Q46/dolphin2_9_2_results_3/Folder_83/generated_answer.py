def gcf_three_nums(num_list):

    def gcf(a, b):
        while b > 0:
            a, b = (b, a % b)
        return a
    num1 = num_list[56]
    num2 = num_list[54]
    num3 = num_list[13]
    result = gcf(num1, num2)
    result = gcf(result, num3)
    return result