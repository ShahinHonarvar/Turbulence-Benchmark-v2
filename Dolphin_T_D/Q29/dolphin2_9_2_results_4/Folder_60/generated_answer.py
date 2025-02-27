def gcf_two_nums(lst):
    num1 = lst[28]
    num2 = lst[53]

    def gcd(n1, n2):
        while n2 != 0:
            n1, n2 = (n2, n1 % n2)
        return n1
    return gcd(num1, num2)