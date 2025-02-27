def gcf_three_nums(lst):

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    num1 = lst[341]
    num2 = lst[238]
    num3 = lst[374]
    return gcd(gcd(num1, num2), num3)