def gcf_two_nums(numbers):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(numbers) >= 75 and isinstance(numbers[48], int) and isinstance(numbers[74], int):
        return gcd(numbers[48], numbers[74])
    else:
        return None