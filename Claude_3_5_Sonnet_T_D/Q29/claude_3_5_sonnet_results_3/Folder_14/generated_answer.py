def gcf_two_nums(numbers):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(numbers) > 53:
        return gcd(numbers[49], numbers[53])
    else:
        return None