def gcf_three_nums(numbers):
    element1 = numbers[67]
    element2 = numbers[84]
    element3 = numbers[13]

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    common_divisor = gcd(element1, gcd(element2, element3))
    return common_divisor