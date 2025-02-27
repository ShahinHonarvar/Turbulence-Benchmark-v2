def all_left_right_truncatable_prime(numbers):
    x = numbers[36]
    primes = [True] * (x + 1)
    primes[0] = primes[1] = False
    p = 2
    while p ** 2 <= x:
        if primes[p]:
            for i in range(p ** 2, x + 1, p):
                primes[i] = False
        p += 1
    left_right_truncatable_primes = []
    for num in range(10, x + 1):
        str_num = str(num)
        if '0' in str_num or not primes[num]:
            continue
        temp_num = str_num
        is_left_right_truncatable_prime = True
        while len(temp_num) > 1:
            if not primes[int(temp_num)] or not primes[int(temp_num[:-1])]:
                is_left_right_truncatable_prime = False
                break
            temp_num = temp_num[1:]
        if is_left_right_truncatable_prime:
            left_right_truncatable_primes.append(num)
    return sorted(left_right_truncatable_primes, reverse=True)