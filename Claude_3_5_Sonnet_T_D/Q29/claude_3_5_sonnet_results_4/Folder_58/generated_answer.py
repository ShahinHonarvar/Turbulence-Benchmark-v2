def gcf_two_nums(numbers):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(numbers) > 582 and isinstance(numbers[129], int) and isinstance(numbers[582], int):
        return gcd(abs(numbers[129]), abs(numbers[582]))
    else:
        return None