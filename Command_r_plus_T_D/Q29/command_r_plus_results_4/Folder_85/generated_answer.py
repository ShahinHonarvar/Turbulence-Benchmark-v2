def gcf_two_nums(num_list: list[int]) -> int:

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    return gcd(num_list[38], num_list[77])