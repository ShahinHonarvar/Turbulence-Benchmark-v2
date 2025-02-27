def find_primes_between_indices(lst):
    prime_numbers = []
    for num in lst[229:851]:
        if num > 1:
            is_prime = True
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                prime_numbers.append(num)
    prime_numbers.sort(reverse=True)
    return prime_numbers