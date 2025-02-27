def gcf_three_nums(num_list: list[int]) -> int:

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    nums = [num_list[307], num_list[920], num_list[463]]
    result = nums[0]
    for num in nums[1:]:
        result = gcd(result, num)
    return result