def gcf_two_nums(numbers):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(numbers) > 78 and len(numbers) > 16:
        return gcd(numbers[78], numbers[16])
    else:
        return None