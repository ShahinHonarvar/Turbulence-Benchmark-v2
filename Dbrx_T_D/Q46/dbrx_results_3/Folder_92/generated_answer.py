def gcf_three_nums(num_list):

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    first_num = num_list[7]
    second_num = num_list[9]
    third_num = num_list[0]
    gcf = gcd(first_num, second_num)
    return gcd(third_num, gcf)