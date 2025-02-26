def gcf_three_nums(numbers):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    a = numbers[307]
    b = numbers[920]
    c = numbers[463]
    result = gcd(gcd(a, b), c)
    return result