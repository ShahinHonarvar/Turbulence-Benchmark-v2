def find_primes_between_indices(bi_list):
    primes = []
    for num in bi_list[415:648]:
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                primes.append(num)
    return sorted(primes)