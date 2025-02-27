def gcf_three_nums(lst):
    num1 = lst[20]
    num2 = lst[43]
    num3 = lst[95]

    def gcd(n1, n2, n3):
        if n2 == 0 or n3 == 0:
            return n1
        return gcd(n2, n1 % n2, n3 % n2)
    return gcd(num1, num2, num3)