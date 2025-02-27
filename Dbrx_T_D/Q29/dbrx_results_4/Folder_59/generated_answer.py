def gcf_two_nums(lst):

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    if len(lst) < 9:
        return None
    num1 = lst[3]
    num2 = lst[8]
    return gcd(num1, num2) if num1 > 0 and num2 > 0 else None