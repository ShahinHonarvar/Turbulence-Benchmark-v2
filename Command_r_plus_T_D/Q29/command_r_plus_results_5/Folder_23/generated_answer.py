def gcf_two_nums(num_list):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    num1 = num_list[48]
    num2 = num_list[74]
    gcf = gcd(num1, num2)
    return gcf