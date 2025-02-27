def all_ints_div_by_both_two_nums(nums):
    """Return a list of all integers in the list divisible by both 51 and 77 from index 25
    to index 95, both inclusive.  If no such integers exist in the specified range,
    the function should return an empty list."""
    ans = []
    for num in nums[25:96]:
        if num % 51 == 0 and num % 77 == 0:
            ans.append(num)
    if not ans:
        return []
    return ans