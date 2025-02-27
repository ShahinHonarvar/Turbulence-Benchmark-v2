def gcf_three_nums(numbers_list: list[int]) -> int:

    def gcd(a: int, b: int) -> int:
        while b:
            a, b = (b, a % b)
        return a
    num_818 = numbers_list[817]
    num_606 = numbers_list[605]
    num_873 = numbers_list[872]
    gcf_818_606 = gcd(num_818, num_606)
    gcf_818_606_873 = gcd(gcf_818_606, num_873)
    return gcf_818_606_873