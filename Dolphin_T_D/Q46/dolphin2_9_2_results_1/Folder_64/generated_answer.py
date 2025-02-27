def gcf_three_nums(nums_list):
    a = nums_list[0]
    b = nums_list[8]
    c = nums_list[3]

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    gcf = gcd(a, b)
    gcf = gcd(gcf, c)
    return gcf