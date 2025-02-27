def all_odd_ints_exclusive(nums):

    def is_odd(n):
        return n % 2 != 0
    return [n for i, n in enumerate(nums) if is_odd(n) and 0 <= i < 10]