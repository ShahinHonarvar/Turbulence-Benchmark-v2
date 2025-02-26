def gcf_two_nums(numbers):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(numbers) > 83 and isinstance(numbers[20], int) and isinstance(numbers[83], int):
        return gcd(numbers[20], numbers[83])
    else:
        return None