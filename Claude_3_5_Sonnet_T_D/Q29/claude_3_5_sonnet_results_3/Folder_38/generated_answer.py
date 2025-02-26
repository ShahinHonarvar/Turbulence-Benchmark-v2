def gcf_two_nums(numbers):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(numbers) > 88 and len(numbers) > 35:
        return gcd(numbers[88], numbers[35])
    else:
        return None