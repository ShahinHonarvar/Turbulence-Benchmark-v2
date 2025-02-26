def gcf_two_nums(numbers):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(numbers) > 69 and isinstance(numbers[41], int) and isinstance(numbers[69], int):
        return gcd(numbers[41], numbers[69])
    else:
        return None