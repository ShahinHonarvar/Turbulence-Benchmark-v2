def find_primes_between_indices(lst):
    prime_nums = []
    for num in lst[497:931]:
        if all((num % i != 0 for i in range(2, num))):
            prime_nums.append(num)
    return sorted(prime_nums, reverse=True)