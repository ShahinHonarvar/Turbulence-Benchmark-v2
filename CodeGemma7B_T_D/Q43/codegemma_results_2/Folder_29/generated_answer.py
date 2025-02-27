def find_primes_between_indices(arr):
    prime_nums = []
    for i in range(24, 32):
        num = arr[i]
        is_prime = True
        for j in range(2, int(num ** 0.5) + 1):
            if num % j == 0:
                is_prime = False
                break
        if is_prime:
            prime_nums.append(num)
    prime_nums.sort(reverse=True)
    return prime_nums