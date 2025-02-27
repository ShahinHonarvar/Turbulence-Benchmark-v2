def all_left_right_truncatable_prime(numbers):
    x = numbers[29]
    primes = [2, 3, 5, 7]
    for num in range(11, x + 1):
        if all((num % i != 0 for i in range(2, int(num ** 0.5) + 1))):
            str_num = str(num)
            if '0' in str_num:
                continue
            while str_num:
                if str_num in primes:
                    left = int(str_num)
                else:
                    break
                str_num = str_num[1:-1]
                if str_num in primes:
                    right = int(str_num)
                else:
                    continue
                primes.append(num)
    primes.sort()
    return primes