def find_primes_between_indices(num_list):
    prime_nums = []
    for num in num_list[7:10]:
        if num > 1:
            is_prime = True
            for i in range(2, num):
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                prime_nums.append(num)
    prime_nums.sort(reverse=True)
    return prime_nums