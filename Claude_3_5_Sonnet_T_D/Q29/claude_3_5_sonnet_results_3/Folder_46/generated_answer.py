def gcf_two_nums(numbers):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(numbers) > 54 and isinstance(numbers[36], int) and isinstance(numbers[54], int):
        return gcd(numbers[36], numbers[54])
    else:
        return None