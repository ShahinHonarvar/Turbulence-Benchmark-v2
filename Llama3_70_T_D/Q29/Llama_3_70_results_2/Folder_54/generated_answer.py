def gcf_two_nums(num_list):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(num_list) > max(56, 92):
        return gcd(num_list[56], num_list[92])
    else:
        return None