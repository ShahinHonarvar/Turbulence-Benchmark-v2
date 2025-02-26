def gcf_two_nums(numbers):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(numbers) > 312:
        return gcd(numbers[180], numbers[312])
    else:
        return None