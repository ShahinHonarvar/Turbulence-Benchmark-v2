def gcf_two_nums(numbers):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(numbers) > 64 and len(numbers) > 28:
        return gcd(numbers[64], numbers[28])
    else:
        return None