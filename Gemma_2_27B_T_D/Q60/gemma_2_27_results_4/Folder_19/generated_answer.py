def all_left_right_truncatable_prime(nums):
    x = nums[67]
    primes = []
    for num in range(x, 1, -1):
        if num > 1:
            is_prime = True
            numstr = str(num)
            for i in range(1, len(numstr)):
                if not (int(numstr[i:]) in [2, 3, 5, 7] and all((int(numstr[j:]) > 1 and int(numstr[j:]) % 2 != 0 and (int(numstr[j:]) % 3 != 0) and (int(numstr[j:]) % 5 != 0) and (int(numstr[j:]) % 7 != 0) for j in range(i, len(numstr))))) or not (int(numstr[:-i]) in [2, 3, 5, 7] and all((int(numstr[:-j]) > 1 and int(numstr[:-j]) % 2 != 0 and (int(numstr[:-j]) % 3 != 0) and (int(numstr[:-j]) % 5 != 0) and (int(numstr[:-j]) % 7 != 0) for j in range(i, len(numstr))))):
                    is_prime = False
                    break
            if is_prime:
                primes.append(num)
    return sorted(primes, reverse=True)