def gcf_three_nums(lst):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    idx1, idx2, idx3 = (412, 932, 337)
    num1, num2, num3 = (lst[idx1], lst[idx2], lst[idx3])
    gcf_12 = gcd(num1, num2)
    return gcd(gcf_12, num3)