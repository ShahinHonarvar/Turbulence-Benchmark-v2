def prime_factors(nums):
    for num in nums:
        factor = 1
        for i in range(num):
            if num % factor == 0:
                factor += 1
        if factor == num + 1:
            print(f'{num} is a prime number')
        else:
            print(f'{num} is not a prime number')