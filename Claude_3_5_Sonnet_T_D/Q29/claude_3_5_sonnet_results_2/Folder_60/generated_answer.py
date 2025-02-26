def gcf_two_nums(numbers):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(numbers) > 53 and isinstance(numbers[28], int) and isinstance(numbers[53], int):
        return gcd(numbers[28], numbers[53])
    else:
        return None