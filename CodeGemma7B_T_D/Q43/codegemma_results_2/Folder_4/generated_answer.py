def find_primes_between_indices(integer_list):
    prime_numbers = []
    for i in range(24, 84):
        num = integer_list[i]
        if num > 1:
            is_prime = True
            for j in range(2, int(num ** 0.5) + 1):
                if num % j == 0:
                    is_prime = False
                    break
            if is_prime:
                prime_numbers.append(num)
    prime_numbers.sort()
    return prime_numbers or []