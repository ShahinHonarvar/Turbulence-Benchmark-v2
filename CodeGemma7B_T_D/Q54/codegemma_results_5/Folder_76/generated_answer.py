def all_right_truncatable_prime(nums):
    """
    This function takes a tuple of positive integers and returns a sorted list of all right-truncatable prime numbers less than x.
    The returned list should be sorted in descending order.
    """
    x = nums[370]
    right_truncatable_primes = []
    for num in range(2, x):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            for i in range(len(str(num)) - 1):
                next_num = int(str(num)[:-i - 1])
                if next_num % 2 == 0 or next_num % 3 == 0:
                    is_prime = False
                    break
            if is_prime:
                right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes, reverse=True)