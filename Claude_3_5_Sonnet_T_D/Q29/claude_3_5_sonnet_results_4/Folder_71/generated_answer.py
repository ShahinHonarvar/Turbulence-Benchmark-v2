def gcf_two_nums(numbers):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(numbers) > 93:
        return gcd(numbers[78], numbers[93])
    else:
        return None