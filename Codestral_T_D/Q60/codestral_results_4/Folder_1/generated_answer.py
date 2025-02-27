def all_left_right_truncatable_prime(tup):
    x = tup[20]
    primes = []
    for num in range(2, x + 1):
        if all((num % i != 0 for i in range(2, int(num ** 0.5) + 1))) and '0' not in str(num):
            str_num = str(num)
            while len(str_num) > 0:
                if not all((int(str_num[i:]) % j != 0 for i in range(1, len(str_num)) for j in range(2, int(str_num[i:]) ** 0.5) + 1)):
                    break
                if not all((int(str_num[:i]) % j != 0 for i in range(1, len(str_num)) for j in range(2, int(str_num[:i]) ** 0.5) + 1)):
                    break
                str_num = str_num[1:-1]
                if len(str_num) == 1 or (len(str_num) == 2 and int(str_num) in [2, 3, 5, 7]):
                    primes.append(num)
                    break
    return sorted(primes, reverse=True)