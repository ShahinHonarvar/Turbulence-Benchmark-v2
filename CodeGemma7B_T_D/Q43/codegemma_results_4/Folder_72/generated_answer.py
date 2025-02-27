def find_primes_between_indices(int_list):
    primes = []
    for num in int_list[28:45]:
        if num > 1:
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    break
            else:
                primes.append(num)
    return sorted(primes) if primes else []