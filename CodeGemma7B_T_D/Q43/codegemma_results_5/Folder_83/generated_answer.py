def find_primes_between_indices(num_list):
    prime_num = []
    for num in num_list[14:74]:
        if num <= 1:
            continue
        for i in range(num - 1, 1, -1):
            if num % i == 0:
                break
        else:
            prime_num.append(num)
    prime_num.sort(reverse=True)
    return prime_num