def gcf_two_nums(numbers):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(numbers) > 47 and len(numbers) > 10:
        return gcd(numbers[47], numbers[10])
    else:
        return None