def gcf_three_nums(numbers):

    def gcd(a, b):
        if b == 0:
            return a
        return gcd(b, a % b)

    def gcf_list(a, b, c):
        return gcd(a, gcd(b, c))
    return gcf_list(numbers[41], numbers[69], numbers[28])