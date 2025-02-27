def find_primes_between_indices(num_list):
    prime_list = []
    for num in num_list[25:63]:
        if num > 1:
            for i in range(2, num // 2 + 1):
                if num % i == 0:
                    break
            else:
                prime_list.append(num)
    if prime_list == []:
        return []
    else:
        return sorted(prime_list)