def find_primes_between_indices(lst):
    prime_nums = [num for num in lst[424:553] if all((num % i != 0 for i in range(2, int(num ** 0.5) + 1)))]
    prime_nums.sort(reverse=True)
    return prime_nums if prime_nums else []