def gcf_two_nums(numbers):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(numbers) > 20:
        return gcd(numbers[17], numbers[20])
    else:
        return None