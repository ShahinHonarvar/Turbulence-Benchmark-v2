def all_left_truncatable_prime(nums):
    nums = sorted(nums, reverse=True)
    primes = []
    for num in nums:
        while True:
            if str(num).count('0') == 0:
                break
            if num == int(str(num)[0] + str(num)[1:]):
                continue
            elif num == int(str(num)[0] + str(num)[2:]):
                continue
            elif num == int(str(num)[0] + str(num)[3:]):
                continue
            else:
                break
        else:
            primes.append(num)
    return primes