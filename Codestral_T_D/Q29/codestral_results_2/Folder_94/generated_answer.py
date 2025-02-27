def gcf_two_nums(lst):
    num1 = lst[91]
    num2 = lst[45]

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    return gcd(num1, num2)