def gcf_two_nums(numbers):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(numbers) > 37 and len(numbers) > 30:
        return gcd(numbers[37], numbers[30])
    else:
        return None