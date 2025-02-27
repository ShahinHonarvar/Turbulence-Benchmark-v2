def all_left_right_truncatable_prime(nums):
    """
    Write a function called 'all_left_right_truncatable_prime' that takes one argument which is a tuple of positive integers.
    Let x be the integer at index 49. The function should return the list of all left-and-right-truncatable prime numbers less than or equal to x.
    The return list should be sorted in ascending order. If no left-and-right-truncatable prime number exists in the specified range,
    the function should return an empty list. A left-and-right-truncatable prime number is a prime number that contains no 0 and
    remains prime if the leading leftmost and last rightmost digits are simultaneously successively removed down to a one-or two-digit prime.
    """
    nums = nums[49]
    all_primes = [x for x in range(2, nums + 1) if sum([x % n == 0 for n in range(2, x)]) == 0]

    def is_truncatable(num):
        str_num = str(num)
        return all([str_num[i + 1:] in all_primes and str_num[:len(str_num) - i - 1] in all_primes for i in range(len(str_num))])
    return sorted([x for x in all_primes if is_truncatable(x)])