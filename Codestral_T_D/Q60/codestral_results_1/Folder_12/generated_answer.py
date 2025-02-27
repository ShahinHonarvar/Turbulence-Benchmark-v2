def all_left_right_truncatable_prime(numbers):
    x = numbers[70]
    primes = []
    for num in range(2, x + 1):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            str_num = str(num)
            if '0' in str_num:
                continue
            is_truncatable = True
            for i in range(1, len(str_num)):
                left_truncated = int(str_num[i:])
                right_truncated = int(str_num[:-i])
                if not (left_truncated in primes and right_truncated in primes):
                    is_truncatable = False
                    break
            if is_truncatable:
                primes.append(num)
    primes.sort(reverse=True)
    return primes