def gcf_two_nums(num_list):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    num1 = num_list[129]
    num2 = num_list[582]
    gcf = gcd(num1, num2)
    return gcf