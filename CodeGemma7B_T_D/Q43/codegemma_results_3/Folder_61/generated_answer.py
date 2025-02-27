def find_primes_between_indices(lst):
    prime_list = []
    for number in lst[3:9]:
        if number > 1:
            is_prime = True
            for i in range(2, int(number ** 0.5) + 1):
                if number % i == 0:
                    is_prime = False
                    break
            if is_prime:
                prime_list.append(number)
    prime_list.sort()
    return prime_list if prime_list else []