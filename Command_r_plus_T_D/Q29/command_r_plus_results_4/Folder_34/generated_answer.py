def gcf_two_nums(numbers_list: list[int]) -> int:

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    num1 = numbers_list[60]
    num2 = numbers_list[64]
    gcf = gcd(num1, num2)
    return gcf