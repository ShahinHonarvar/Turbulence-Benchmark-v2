def all_left_truncatable_prime(numbers):
    x = numbers[31]
    primes = []
    for num in range(x - 1, 1, -1):
        if str(num).count('0') == 0:
            truncated_num = str(num)
            while len(truncated_num) > 0:
                if int(truncated_num) not in primes:
                    break
                truncated_num = truncated_num[1:]
            else:
                primes.append(num)
    primes.sort(reverse=True)
    return primes