def gcf_two_nums(numbers):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(numbers) > 51 and len(numbers) > 31:
        return gcd(numbers[51], numbers[31])
    else:
        return None