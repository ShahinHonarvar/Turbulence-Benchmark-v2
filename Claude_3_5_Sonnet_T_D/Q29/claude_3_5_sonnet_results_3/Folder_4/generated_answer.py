def gcf_two_nums(numbers):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(numbers) > 76 and len(numbers) > 57:
        return gcd(numbers[76], numbers[57])
    else:
        return None