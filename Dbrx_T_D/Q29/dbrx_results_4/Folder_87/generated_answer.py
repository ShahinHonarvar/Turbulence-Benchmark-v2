def gcf_two_nums(numbers_list):

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return abs(a)
    return gcd(numbers_list[83], numbers_list[14]) if len(numbers_list) > 83 and len(numbers_list) > 14 else None