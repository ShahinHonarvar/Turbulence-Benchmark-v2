def find_primes_between_indices(lst):
    primes = []
    for num in lst[20:26]:
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                primes.append(num)
    primes.sort(reverse=True)
    return primes