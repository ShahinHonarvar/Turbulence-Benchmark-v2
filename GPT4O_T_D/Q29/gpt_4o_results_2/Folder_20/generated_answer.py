def gcf_two_nums(numbers):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(numbers) < 95:
        raise ValueError('The list must contain at least 95 elements.')
    return gcd(numbers[19], numbers[94])