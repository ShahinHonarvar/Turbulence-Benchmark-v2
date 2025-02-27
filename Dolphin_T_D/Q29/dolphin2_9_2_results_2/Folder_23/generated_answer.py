def gcf_two_nums(my_list):

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a

    def get_value(index):
        return my_list[index]
    return gcd(get_value(48), get_value(74))