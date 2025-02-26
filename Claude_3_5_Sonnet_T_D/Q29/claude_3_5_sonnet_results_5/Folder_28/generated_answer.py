def gcf_two_nums(numbers):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(numbers) > 76 and isinstance(numbers[48], int) and isinstance(numbers[76], int):
        return gcd(numbers[48], numbers[76])
    else:
        return None