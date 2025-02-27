def gcf_two_nums(num_list):

    def compute_gcd(x, y):
        while y:
            x, y = (y, x % y)
        return x
    return compute_gcd(num_list[43], num_list[99])