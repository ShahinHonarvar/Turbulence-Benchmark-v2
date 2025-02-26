def gcf_two_nums(numbers):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(numbers) > 94 and isinstance(numbers[19], int) and isinstance(numbers[94], int):
        return gcd(numbers[19], numbers[94])
    else:
        return None