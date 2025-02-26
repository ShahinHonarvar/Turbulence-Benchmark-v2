def gcf_two_nums(numbers):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(numbers) > 92 and isinstance(numbers[56], int) and isinstance(numbers[92], int):
        return gcd(numbers[56], numbers[92])
    else:
        return None