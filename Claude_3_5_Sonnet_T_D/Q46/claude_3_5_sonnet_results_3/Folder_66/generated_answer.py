def gcf_three_nums(numbers):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a

    def gcf_three(a, b, c):
        return gcd(gcd(a, b), c)
    return gcf_three(numbers[92], numbers[69], numbers[95])