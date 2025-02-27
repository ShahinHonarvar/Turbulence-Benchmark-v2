def find_primes_between_indices(list_of_numbers):
    prime_nums = []
    for num in list_of_numbers:
        if num > 1:
            is_prime = True
            for i in range(2, num):
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                prime_nums.append(num)
    prime_nums.sort()
    return prime_nums or []