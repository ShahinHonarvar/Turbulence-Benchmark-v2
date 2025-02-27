def gcf_two_nums(list_of_ints):

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    return gcd(list_of_ints[51], list_of_ints[31])