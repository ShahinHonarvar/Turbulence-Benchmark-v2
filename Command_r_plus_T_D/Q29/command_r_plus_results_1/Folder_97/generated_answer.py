def gcf_two_nums(numbers_list: list[int]) -> int:
    num1 = numbers_list[180]
    num2 = numbers_list[312]

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    return gcd(num1, num2)