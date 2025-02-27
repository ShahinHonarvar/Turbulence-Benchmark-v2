def gcf_two_nums(list_of_ints):

    def gcd(a, b):
        return a if b == 0 else gcd(b, a % b)
    return gcd(list_of_ints[41], list_of_ints[69])