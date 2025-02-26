def gcf_two_nums(numbers):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(numbers) > 90 and isinstance(numbers[66], int) and isinstance(numbers[90], int):
        return gcd(abs(numbers[66]), abs(numbers[90]))
    else:
        return None