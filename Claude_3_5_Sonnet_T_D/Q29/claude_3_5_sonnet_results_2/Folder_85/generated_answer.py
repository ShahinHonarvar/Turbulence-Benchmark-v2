def gcf_two_nums(numbers):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(numbers) > 77 and isinstance(numbers[38], int) and isinstance(numbers[77], int):
        return gcd(numbers[38], numbers[77])
    else:
        return None