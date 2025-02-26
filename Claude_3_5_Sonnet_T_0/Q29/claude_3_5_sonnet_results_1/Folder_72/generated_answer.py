def gcf_two_nums(numbers):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(numbers) > 37 and isinstance(numbers[18], int) and isinstance(numbers[37], int):
        return gcd(numbers[18], numbers[37])
    else:
        return None