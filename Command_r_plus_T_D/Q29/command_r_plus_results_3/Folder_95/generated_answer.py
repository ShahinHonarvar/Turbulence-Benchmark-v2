def gcf_two_nums(num_list: list[int]) -> int:

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    num1 = num_list[43]
    num2 = num_list[99]
    return gcd(num1, num2)