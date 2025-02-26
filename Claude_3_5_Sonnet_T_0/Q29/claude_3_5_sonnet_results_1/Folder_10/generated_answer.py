def gcf_two_nums(numbers):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(numbers) > 99 and isinstance(numbers[15], int) and isinstance(numbers[99], int):
        return gcd(numbers[15], numbers[99])
    else:
        return None