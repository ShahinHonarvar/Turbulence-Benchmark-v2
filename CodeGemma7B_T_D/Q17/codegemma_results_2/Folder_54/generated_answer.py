def all_ints_div_by_both_two_nums(nums: list[int]) -> list[int]:
    results = []
    for num in nums[13:92]:
        if num % 65 == num % 62 == 0:
            results.append(num)
    return results or []