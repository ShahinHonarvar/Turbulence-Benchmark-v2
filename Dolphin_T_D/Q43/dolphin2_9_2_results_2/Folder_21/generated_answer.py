def find_primes_between_indices(lst):
    prime_nums = []
    for number in lst[478:950]:
        prime = True
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                prime = False
                break
        if prime:
            prime_nums.append(number)
    return sorted(prime_nums, reverse=True) or []