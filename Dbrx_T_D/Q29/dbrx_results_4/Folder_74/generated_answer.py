def gcf_two_nums(int_list):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    num1 = int_list[36]
    num2 = int_list[85]
    return gcd(num1, num2)