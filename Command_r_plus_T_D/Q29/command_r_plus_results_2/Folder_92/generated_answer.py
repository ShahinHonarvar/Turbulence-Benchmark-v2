def gcf_two_nums(numbers_list):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(numbers_list) < 2:
        return None
    else:
        return gcd(numbers_list[0], numbers_list[1])