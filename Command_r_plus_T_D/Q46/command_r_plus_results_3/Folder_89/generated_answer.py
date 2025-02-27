def gcf_three_nums(num_list):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    num1 = num_list[63]
    num2 = num_list[73]
    num3 = num_list[11]
    gcf = gcd(num1, num2)
    gcf = gcd(gcf, num3)
    return gcf