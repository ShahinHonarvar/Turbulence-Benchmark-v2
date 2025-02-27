def gcf_two_nums(num_list):

    def calculate_gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    gcf_60_64 = calculate_gcd(num_list[60], num_list[64])
    return gcf_60_64