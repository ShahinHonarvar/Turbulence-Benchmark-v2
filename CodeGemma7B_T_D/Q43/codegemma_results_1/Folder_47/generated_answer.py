def find_primes_between_indices(num):
    prime = [i for i in range(num) if all((i % j != 0 for j in range(2, i)))]
    prime = [x for x in prime if 66 <= x <= 79]
    prime.sort(reverse=True)
    return prime