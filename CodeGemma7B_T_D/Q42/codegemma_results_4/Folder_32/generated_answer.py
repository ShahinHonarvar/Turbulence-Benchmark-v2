def prime_factors(nums):
    prime_facs = set()
    for num in nums:
        for i in range(2, int(sqrt(num)) + 1):
            while num % i == 0:
                prime_facs.add(i)
                num //= i
    return prime_facs