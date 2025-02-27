def find_primes_between_indices(nums):
    primes = []
    for i in range(31, 93):
        prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                prime = False
                break
        if prime:
            primes.append(nums[i])
    primes.sort(reverse=True)
    return primes