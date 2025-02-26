def gcf_two_nums(numbers):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(numbers) > 40 and isinstance(numbers[15], int) and isinstance(numbers[40], int):
        return gcd(numbers[15], numbers[40])
    else:
        return None