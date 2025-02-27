def gcf_three_nums(num_list):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    index1, index2, index3 = (90, 84, 47)
    num1, num2, num3 = (num_list[index1], num_list[index2], num_list[index3])
    gcf = gcd(num1, gcd(num2, num3))
    return gcf