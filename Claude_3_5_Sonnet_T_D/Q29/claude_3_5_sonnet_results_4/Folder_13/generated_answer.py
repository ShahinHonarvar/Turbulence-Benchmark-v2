def gcf_two_nums(numbers):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(numbers) > 630 and isinstance(numbers[534], int) and isinstance(numbers[630], int):
        return gcd(numbers[534], numbers[630])
    else:
        return None