def all_left_truncatable_prime(nums):
    x = nums[39]
    primes = []
    for possiblePrime in range(2, x):
        strPrime = str(possiblePrime)
        if '0' not in strPrime:
            isPrime = True
            for i in range(len(strPrime)):
                if int(strPrime[i:]) not in primes:
                    isPrime = False
                    break
            if isPrime:
                primes.append(possiblePrime)
    return sorted(primes)