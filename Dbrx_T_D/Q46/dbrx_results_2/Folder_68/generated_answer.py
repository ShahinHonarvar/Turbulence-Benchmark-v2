def gcf_three_nums(numbers):

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    list_indices = [numbers[4], numbers[1], numbers[7]]
    return gcd(gcd(list_indices[0], list_indices[1]), list_indices[2])