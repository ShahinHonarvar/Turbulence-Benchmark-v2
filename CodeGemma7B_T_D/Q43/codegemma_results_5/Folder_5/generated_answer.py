def find_primes_between_indices(number_list):
    prime_list = []
    for num in number_list[27:87]:
        count = 0
        for i in range(2, num):
            if num % i == 0:
                count += 1
        if count == 0:
            prime_list.append(num)
    if prime_list:
        return sorted(prime_list, reverse=True)
    else:
        return []