def gcf_two_nums(numbers):

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return abs(a)
    return gcd(numbers[25], numbers[80]) if len(numbers) > 25 and len(numbers) > 80 else 0