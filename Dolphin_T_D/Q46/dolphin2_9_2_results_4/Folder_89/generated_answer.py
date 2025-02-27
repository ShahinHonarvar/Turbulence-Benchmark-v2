def gcf_three_nums(lst):
    if not all((isinstance(i, int) and i > 0 for i in lst)):
        raise ValueError('The list must contain only positive integers')
    num1 = lst[63]
    num2 = lst[73]
    num3 = lst[11]

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    return gcd(gcd(num1, num2), num3)