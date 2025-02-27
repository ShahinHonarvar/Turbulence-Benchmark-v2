def gcf_two_nums(numbers):

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    return gcd(numbers[21], numbers[17]) if len(numbers) > 17 else None