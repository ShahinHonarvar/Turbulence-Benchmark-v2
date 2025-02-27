def find_primes_between_indices(lst):
    primes = []
    for i in range(32, 36):
        if 0 < i < len(lst):
            num = abs(lst[i])
            if num > 1:
                for j in range(2, num):
                    if num % j == 0:
                        break
                else:
                    primes.append(num)
    return sorted(primes)