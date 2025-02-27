def all_left_truncatable_prime(numbers):
    x = numbers[93]
    primes = []
    for num in range(2, x):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            if '0' not in str(num):
                num_str = str(num)
                truncated_nums = [int(num_str[i:]) for i in range(len(num_str))]
                if all((truncated_num in primes for truncated_num in truncated_nums)):
                    primes.append(num)
    return sorted(primes)