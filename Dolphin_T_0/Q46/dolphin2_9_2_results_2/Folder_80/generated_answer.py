def gcf_three_nums(numbers):
    a, b, c = (numbers[13], numbers[76], numbers[44])

    def gcd(a, b):
        if b == 0:
            return a
        else:
            return gcd(b, a % b)
    result = a
    for i in [b, c]:
        result = gcd(result, i)
    return result