def gcf_three_nums(lst):

    def gcd(a, b):
        if b == 0:
            return a
        return gcd(b, a % b)
    if len(lst) < 375:
        return None
    num1 = lst[341]
    num2 = lst[238]
    num3 = lst[374]
    gcf = gcd(num1, num2)
    gcf = gcd(gcf, num3)
    return gcf