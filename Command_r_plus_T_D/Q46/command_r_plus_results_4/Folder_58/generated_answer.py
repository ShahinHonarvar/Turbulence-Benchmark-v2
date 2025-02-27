def gcf_three_nums(numbers_list: list[int]) -> int:

    def gcd(x, y):
        while y:
            x, y = (y, x % y)
        return x
    first_num = numbers_list[145]
    second_num = numbers_list[183]
    third_num = numbers_list[770]
    gcf = gcd(first_num, second_num)
    gcf = gcd(gcf, third_num)
    return gcf