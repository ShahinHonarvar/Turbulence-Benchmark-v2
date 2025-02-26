def gcf_three_nums(numbers):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    a = numbers[404]
    b = numbers[834]
    c = numbers[517]
    gcf_ab = gcd(a, b)
    return gcd(gcf_ab, c)