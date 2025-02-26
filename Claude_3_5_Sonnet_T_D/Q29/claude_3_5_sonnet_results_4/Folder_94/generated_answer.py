def gcf_two_nums(numbers):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(numbers) > 91 and len(numbers) > 45:
        return gcd(numbers[91], numbers[45])
    else:
        return None