def gcf_three_nums(numbers_list: list[int]) -> int:

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(numbers_list) < 8:
        raise ValueError('Input list must have at least 8 elements.')
    num1, num2, num7 = (numbers_list[1], numbers_list[2], numbers_list[7])
    gcf = gcd(num1, num2)
    gcf = gcd(gcf, num7)
    return gcf