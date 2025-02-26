def gcf_two_nums(numbers):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(numbers) > 34 and isinstance(numbers[27], int) and isinstance(numbers[34], int) and (numbers[27] > 0) and (numbers[34] > 0):
        return gcd(numbers[27], numbers[34])
    else:
        return None