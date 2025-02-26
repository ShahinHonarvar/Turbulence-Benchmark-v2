def gcf_two_nums(numbers):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(numbers) > 72 and isinstance(numbers[33], int) and isinstance(numbers[72], int):
        return gcd(numbers[33], numbers[72])
    else:
        return None