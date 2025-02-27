import math

def find_primes_between_indices(lst):
    primes = []
    for num in lst[59:96]:
        if num > 1:
            is_prime = True
            for i in range(2, int(math.sqrt(num)) + 1):
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                primes.append(num)
    if len(primes) == 0:
        return []
    else:
        return sorted(primes)