def gcf_two_nums(numbers):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(numbers) > 166 and len(numbers) > 106:
        return gcd(numbers[166], numbers[106])
    else:
        return None