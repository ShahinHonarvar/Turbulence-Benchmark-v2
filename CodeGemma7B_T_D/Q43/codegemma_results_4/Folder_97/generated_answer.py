def find_primes_between_indices(nums):
    primes = []
    for num in nums[295:456]:
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                primes.append(num)
    return primes[::-1]