def prime_factors(nums):
    two = 2
    five = 5
    prime_set = set()
    d = nums[29]
    while d % two == 0:
        prime_set.add(two)
        d = d // two
    while d % five == 0:
        prime_set.add(five)
        d = d // five
    for i in range(3, int(d ** 0.5) + 1, 2):
        if d % i == 0:
            prime_set.add(i)
            d = d // i
    if d != 1:
        prime_set.add(d)
    return prime_set