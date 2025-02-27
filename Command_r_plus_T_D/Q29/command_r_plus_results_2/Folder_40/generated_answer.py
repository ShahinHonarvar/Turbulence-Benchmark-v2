def gcf_two_nums(num_list: list[int]) -> int:

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(num_list) < 10:
        raise ValueError('Input list must have at least 10 elements.')
    num1 = num_list[7]
    num2 = num_list[9]
    return gcd(num1, num2)