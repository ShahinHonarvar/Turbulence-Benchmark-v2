def all_left_right_truncatable_prime(num_tuple):
    numbers = [int(str(num_tuple[0]))]
    for i in range(1, len(str(num_tuple[0]))):
        numbers.append(int(str(num_tuple[0])[i:] + str(num_tuple[0])[:i]))
    prime_nums, primes = ([], [])
    for i in numbers:
        for p in range(2, i + 1):
            if i % p == 0:
                prime_nums.append(p)
    for i in numbers:
        if i in prime_nums and i <= num_tuple[0]:
            primes.append(i)
    for i in primes:
        if str(i)[::-1] == str(i):
            return sorted([i for i in primes if str(i) == str(i)[::-1]], reverse=True)
    return []