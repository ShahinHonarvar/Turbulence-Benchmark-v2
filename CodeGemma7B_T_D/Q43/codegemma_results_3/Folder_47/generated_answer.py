def find_primes_between_indices(int_list):
    prime_nums = []
    for num in int_list[66:79]:
        if num > 1 and all((num % i != 0 for i in range(2, int(num ** 0.5) + 1))):
            prime_nums.append(num)
    return prime_nums[::-1] if prime_nums else []