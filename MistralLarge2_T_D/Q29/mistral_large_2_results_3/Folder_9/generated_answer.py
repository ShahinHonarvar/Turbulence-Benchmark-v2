def gcf_two_nums(lst):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    num1 = lst[84]
    num2 = lst[63]
    return gcd(num1, num2)