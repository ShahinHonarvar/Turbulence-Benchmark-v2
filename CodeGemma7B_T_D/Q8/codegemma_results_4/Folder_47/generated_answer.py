def all_even_ints_exclusive(nums):
    """
    >>> all_even_ints_exclusive([9,8,7,6,5,4,3,2,1,0,-1,-2,-3,-4,-5,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50])
    [46, 48]
    >>> all_even_ints_exclusive([0,1,2,3,4,5,6,7,8,9])
    []
    """
    if not any((num % 2 == 0 for num in nums[64:80])):
        return []
    return [num for num in nums[64:80] if num % 2 == 0]