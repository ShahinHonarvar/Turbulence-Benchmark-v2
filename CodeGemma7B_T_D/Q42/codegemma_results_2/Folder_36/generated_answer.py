def prime_factors(nums):
    """
    This function takes a list of positive integers and returns the set of all prime factors of the integer at index 990.
    """
    prime_factors_set = set()
    prime_factors_set2 = set()
    for i in range(2, nums[990] + 1):
        while nums[990] % i == 0:
            while nums[990] % i == 0:
                prime_factors_set.add(i)
                nums[990] //= i
    for a in prime_factors_set:
        if prime_factors_set.intersection(prime_factors_set2) == set():
            prime_factors_set2.add(a)
    return prime_factors_set2