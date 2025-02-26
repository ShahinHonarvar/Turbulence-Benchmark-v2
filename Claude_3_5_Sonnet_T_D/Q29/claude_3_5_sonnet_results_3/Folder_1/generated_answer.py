def gcf_two_nums(numbers):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(numbers) > 66 and isinstance(numbers[13], int) and isinstance(numbers[66], int):
        return gcd(abs(numbers[13]), abs(numbers[66]))
    else:
        return None