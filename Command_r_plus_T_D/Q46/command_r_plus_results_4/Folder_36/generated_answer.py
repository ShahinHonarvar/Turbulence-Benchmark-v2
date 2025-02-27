def gcf_three_nums(num_list: list[int]) -> int:

    def gcd(a: int, b: int) -> int:
        while b:
            a, b = (b, a % b)
        return a
    nums = [num_list[427], num_list[761], num_list[148]]
    result = nums[0]
    for num in nums[1:]:
        result = gcd(result, num)
    return result