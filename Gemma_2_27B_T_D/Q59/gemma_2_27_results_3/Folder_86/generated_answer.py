def all_left_truncatable_prime(numbers):
    x = numbers[126]
    primes = []
    for num in range(x, 1, -1):
        is_prime = True
        str_num = str(num)
        for i in range(len(str_num)):
            if int(str_num[i:]) not in {2, 3, 5, 7}:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return sorted(primes, reverse=True)