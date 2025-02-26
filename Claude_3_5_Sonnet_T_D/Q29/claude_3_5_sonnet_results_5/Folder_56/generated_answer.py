def gcf_two_nums(numbers):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(numbers) > 84 and len(numbers) > 13:
        return gcd(numbers[84], numbers[13])
    else:
        return None