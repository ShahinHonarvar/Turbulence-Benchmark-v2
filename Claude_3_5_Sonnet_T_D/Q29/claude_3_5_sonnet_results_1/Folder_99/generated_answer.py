def gcf_two_nums(numbers):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(numbers) > 812 and isinstance(numbers[279], int) and isinstance(numbers[812], int):
        return gcd(numbers[279], numbers[812])
    else:
        return None