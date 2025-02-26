def gcf_two_nums(numbers):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(numbers) > 69 and len(numbers) > 40:
        return gcd(numbers[69], numbers[40])
    else:
        return None