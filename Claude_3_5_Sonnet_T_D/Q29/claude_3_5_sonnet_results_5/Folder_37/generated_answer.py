def gcf_two_nums(numbers):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(numbers) > 74:
        return gcd(numbers[29], numbers[74])
    else:
        return None