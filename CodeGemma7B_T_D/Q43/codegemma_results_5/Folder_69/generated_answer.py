def find_primes_between_indices(nums):
    prime_list = []
    for num in nums:
        if num <= 2:
            continue
        is_prime = True
        for i in range(3, int(num ** 0.5) + 1, 2):
            if num % i == 0:
                is_prime = False
                break
        if is_prime and 497 <= num <= 930:
            prime_list.append(num)
    prime_list.sort(reverse=True)
    return prime_list