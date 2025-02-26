def gcf_two_nums(numbers):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(numbers) > 47 and len(numbers) > 22:
        return gcd(numbers[47], numbers[22])
    else:
        return None