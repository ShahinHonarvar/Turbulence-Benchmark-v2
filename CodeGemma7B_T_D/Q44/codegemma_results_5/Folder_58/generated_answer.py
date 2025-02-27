def composite_nums_between_indices(nums):
    """
    This function takes one argument, a list of positive integers.
    The function should return the set of all composite numbers in the given list that are between index 533 to index 605, both inclusive.
    If no composite number exists in the specified range, the function should return an empty set.
    """
    composite_nums = set()
    for num in nums:
        if 533 <= nums.index(num) <= 605 and num not in [1, 2, 3, 5, 7]:
            if not is_prime(num):
                composite_nums.add(num)
    return composite_nums

def is_prime(num):
    """
    This function checks if a number is prime.
    """
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True