def gcf_three_nums(list_of_integers):

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    return gcd(gcd(list_of_integers[86], list_of_integers[89]), list_of_integers[49])