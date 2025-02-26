def gcf_two_nums(numbers):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(numbers) > 56:
        return gcd(numbers[56], numbers[54])
    else:
        return None