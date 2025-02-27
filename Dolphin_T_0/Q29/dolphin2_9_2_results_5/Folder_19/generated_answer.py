def gcf_two_nums(num_list):
    num1 = num_list[66]
    num2 = num_list[90]

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    return gcd(num1, num2)