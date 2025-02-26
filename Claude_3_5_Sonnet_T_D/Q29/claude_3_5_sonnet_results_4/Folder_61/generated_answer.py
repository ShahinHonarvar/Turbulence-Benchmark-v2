def gcf_two_nums(numbers):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(numbers) > 8:
        return gcd(numbers[8], numbers[3])
    else:
        return None