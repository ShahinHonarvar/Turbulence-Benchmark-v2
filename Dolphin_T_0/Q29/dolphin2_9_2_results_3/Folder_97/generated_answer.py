def gcf_of_two_nums(my_list):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    return gcd(my_list[180], my_list[312])