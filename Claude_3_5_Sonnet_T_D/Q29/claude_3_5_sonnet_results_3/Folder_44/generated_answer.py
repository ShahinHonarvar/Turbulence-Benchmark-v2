def gcf_two_nums(numbers):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(numbers) > 88 and isinstance(numbers[56], int) and isinstance(numbers[88], int):
        return gcd(numbers[56], numbers[88])
    else:
        return None