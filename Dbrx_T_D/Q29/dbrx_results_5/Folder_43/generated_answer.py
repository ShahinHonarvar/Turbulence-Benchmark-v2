def gcf_two_nums(lst):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    num1 = lst[59]
    num2 = lst[93]
    factor = gcd(num1, num2)
    return factor if factor != 1 else -1