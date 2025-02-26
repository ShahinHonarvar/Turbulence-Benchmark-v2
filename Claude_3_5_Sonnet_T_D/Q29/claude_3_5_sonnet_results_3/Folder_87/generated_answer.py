def gcf_two_nums(numbers):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(numbers) > 83 and len(numbers) > 14:
        return gcd(numbers[83], numbers[14])
    else:
        return None