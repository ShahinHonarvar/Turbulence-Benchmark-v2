def gcf_two_nums(numbers):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(numbers) > 90 and len(numbers) > 41:
        return gcd(numbers[90], numbers[41])
    else:
        return None