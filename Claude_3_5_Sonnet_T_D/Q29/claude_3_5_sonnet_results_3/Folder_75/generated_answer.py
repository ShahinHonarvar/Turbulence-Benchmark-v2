def gcf_two_nums(numbers):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(numbers) > 42 and len(numbers) > 25:
        return gcd(numbers[42], numbers[25])
    else:
        return None