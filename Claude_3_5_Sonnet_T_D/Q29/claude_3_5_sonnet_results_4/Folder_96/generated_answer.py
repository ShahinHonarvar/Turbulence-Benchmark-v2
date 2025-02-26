def gcf_two_nums(numbers):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(numbers) > 95 and len(numbers) > 73:
        return gcd(numbers[95], numbers[73])
    else:
        return None