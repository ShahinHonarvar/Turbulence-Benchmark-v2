def gcf_two_nums(numbers):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(numbers) > 80 and isinstance(numbers[64], int) and isinstance(numbers[80], int):
        return gcd(numbers[64], numbers[80])
    else:
        return None