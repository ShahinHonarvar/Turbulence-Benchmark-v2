def all_left_truncatable_prime(numbers):
    x = numbers[126]
    left_truncatable_primes = []
    for num in range(2, x):
        if str(num).find('0') != -1:
            continue
        is_left_truncatable_prime = True
        str_num = str(num)
        for i in range(1, len(str_num)):
            if int(str_num[i:]) not in left_truncatable_primes:
                is_left_truncatable_prime = False
                break
        if is_left_truncatable_prime:
            left_truncatable_primes.append(num)
    left_truncatable_primes.sort(reverse=True)
    return left_truncatable_primes