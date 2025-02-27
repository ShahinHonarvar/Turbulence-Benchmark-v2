def gcf_three_nums(numbers):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    gcf = gcd(numbers[7], gcd(numbers[6], numbers[8]))
    return gcf