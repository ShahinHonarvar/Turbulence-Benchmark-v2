def gcf_two_nums(num_list):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    num1 = num_list[380]
    num2 = num_list[327]
    return gcd(num1, num2)