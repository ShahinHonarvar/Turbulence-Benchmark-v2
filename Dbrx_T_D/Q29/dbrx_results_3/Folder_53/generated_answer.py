def gcf_two_nums(numbers):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    factor_28 = numbers[28]
    factor_67 = numbers[67]
    while factor_67:
        factor_28, factor_67 = (factor_67, factor_28 % factor_67)
    return factor_28