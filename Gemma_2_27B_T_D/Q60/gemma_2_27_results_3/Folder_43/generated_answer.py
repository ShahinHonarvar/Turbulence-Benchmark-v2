def all_left_right_truncatable_prime(nums):
    x = nums[89]
    primes = []
    for num in range(2, x + 1):
        if all((int(str(num)[i:]) in [2, 3, 5, 7] for i in range(len(str(num))))):
            prime = True
            for i in range(len(str(num))):
                if int(str(num)[:len(str(num)) - i]) not in [2, 3, 5, 7] or int(str(num)[i:]) not in [2, 3, 5, 7]:
                    prime = False
                    break
            if prime:
                primes.append(num)
    return sorted(primes, reverse=True)