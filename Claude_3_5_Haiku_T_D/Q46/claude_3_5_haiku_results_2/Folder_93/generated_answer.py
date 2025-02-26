def gcf_three_nums(numbers):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    a, b, c = (numbers[25], numbers[76], numbers[57])
    first_gcf = gcd(a, b)
    final_gcf = gcd(first_gcf, c)
    return final_gcf