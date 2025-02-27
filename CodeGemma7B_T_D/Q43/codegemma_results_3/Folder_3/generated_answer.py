def find_primes_between_indices(nums):
    prime_nums = []
    for num in nums[80:85]:
        if num % 2 != 0 and num % 3 != 0 and (num % 5 != 0) and (num % 7 != 0):
            prime_nums.append(num)
    prime_nums.sort(reverse=True)
    return prime_nums