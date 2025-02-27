def gcf_three_nums(lst):
    a = lst[341]
    b = lst[238]
    c = lst[374]

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    return gcd(gcd(a, b), c)