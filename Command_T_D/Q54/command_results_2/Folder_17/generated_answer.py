import itertools

def all_right_truncatable_prime(nums):
    return sorted(list(filter(lambda x: x.isprime() and x.isrighttruncatable(), itertools.takewhile(lambda x: x < nums[36], itertools.permutations(range(2, int(nums[36]) + 1)))), reverse=True))