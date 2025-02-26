def gcf_two_nums(numbers):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(numbers) > 46 and len(numbers) >= 14:
        return gcd(numbers[46], numbers[13])
    else:
        return None