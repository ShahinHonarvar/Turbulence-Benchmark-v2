def all_left_right_truncatable_prime(t):
    x = t[25]
    primes = []
    for num in range(x, 1, -1):
        if all((num % i != 0 for i in range(2, int(num ** 0.5) + 1))):
            str_num = str(num)
            if '0' not in str_num:
                while len(str_num) > 1:
                    new_num = int(str_num[1:len(str_num) - 1])
                    if all((new_num % i != 0 for i in range(2, int(new_num ** 0.5) + 1))):
                        str_num = str(new_num)
                    else:
                        break
                else:
                    primes.append(num)
    return sorted(primes, reverse=True)