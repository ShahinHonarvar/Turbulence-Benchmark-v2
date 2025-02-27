def gcf_two_nums(number_list):

    def gcd(a, b):
        while b != 0:
            temp = a
            a = b
            b = temp % b
        return a
    return gcd(number_list[51], number_list[27])