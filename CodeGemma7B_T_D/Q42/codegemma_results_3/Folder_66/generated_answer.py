def prime_factors(nums):
    return set(factors(nums[42]))

def factors(n):
    fs = []
    i = 2
    while i * i <= n:
        while n % i == 0:
            fs.append(i)
            n //= i
        i += 1
    if n > 1:
        fs.append(n)
    return fs