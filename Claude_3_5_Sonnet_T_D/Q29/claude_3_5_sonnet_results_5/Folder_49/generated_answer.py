def gcf_two_nums(numbers):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(numbers) > 28 and len(numbers) > 20:
        return gcd(numbers[28], numbers[20])
    else:
        return None