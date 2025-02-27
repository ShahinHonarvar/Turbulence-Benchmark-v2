def all_right_truncatable_prime(nums):
    """
    Write a function called 'all_right_truncatable_prime' that takes an argument which is a tuple of positive integers.
    Let x be the integer at index 429. The function should return the sorted list of all right-truncatable prime numbers less than x.
    The returned list should be sorted in descending order. If there is no such right-truncatable prime number, the function should return an empty list.
    A right-truncatable prime number is a prime number that remains prime when the last rightmost digit is successively removed.
    """
    x = nums[429]

    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_right_truncatable(num):
        str_num = str(num)
        for i in range(1, len(str_num)):
            trunc_num = int(str_num[:-i])
            if not is_prime(trunc_num):
                return False
        return True
    result = sorted([p for p in range(2, x) if is_prime(p) and is_right_truncatable(p)], reverse=True)
    return result if result else []