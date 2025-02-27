def all_even_ints_exclusive(nums):
    """Function takes list of ints and returns list of even ints from index 0 to index 4, exclusive"""
    even_nums = []
    for num in nums:
        if num % 2 == 0 and num >= 0 and (num < 5):
            even_nums.append(num)
    return even_nums