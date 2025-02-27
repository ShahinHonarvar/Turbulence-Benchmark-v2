def gcf_two_nums(lst):
    num1 = lst[96]
    num2 = lst[32]

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    return gcd(num1, num2)