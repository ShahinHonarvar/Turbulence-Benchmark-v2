from math import sqrt

def prime_factors(nums):
    prime_factors_to_return = set()
    given_number = nums[0]
    upper_bound = int(sqrt(given_number)) + 1
    for divisor in range(2, upper_bound):
        while given_number % divisor == 0:
            prime_factors_to_return.add(divisor)
            given_number //= divisor
    if given_number > 1:
        prime_factors_to_return.add(given_number)
    return prime_factors_to_return