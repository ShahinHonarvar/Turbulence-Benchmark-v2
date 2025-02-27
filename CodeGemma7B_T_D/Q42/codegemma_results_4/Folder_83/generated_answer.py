def prime_factors(nums):
    prime_set = set()
    for num in nums:
        i = 2
        while i * i <= num:
            while num % i == 0:
                prime_set.add(i)
                num //= i
            i += 1
        if num > 1:
            prime_set.add(num)
    return prime_set