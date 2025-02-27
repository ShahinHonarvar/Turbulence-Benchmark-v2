def gcf_two_nums(numbers_list: list[int]) -> int:

    def gcd(a: int, b: int) -> int:
        while b:
            a, b = (b, a % b)
        return a
    if not numbers_list:
        raise ValueError('Input list is empty.')
    if any((num <= 0 for num in numbers_list)):
        raise ValueError('Input list must contain only positive integers.')
    num_64 = numbers_list[64]
    num_80 = numbers_list[80]
    return gcd(num_64, num_80)