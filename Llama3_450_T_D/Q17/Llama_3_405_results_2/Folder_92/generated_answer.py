def all_ints_div_by_both_two_nums(nums):

    def is_divisible(n, start, end):
        for i in range(start, end + 1):
            if n % i != 0:
                return False
        return True
    result = []
    for num in nums:
        if is_divisible(num, 1, -1):
            result.append(num)
    return result[:1]