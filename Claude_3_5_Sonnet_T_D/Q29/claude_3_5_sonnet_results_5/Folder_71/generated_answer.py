def gcf_two_nums(numbers):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(numbers) > 93 and isinstance(numbers[78], int) and isinstance(numbers[93], int):
        return gcd(numbers[78], numbers[93])
    else:
        return None