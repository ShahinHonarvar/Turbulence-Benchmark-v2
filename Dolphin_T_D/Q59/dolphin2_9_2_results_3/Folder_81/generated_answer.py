def all_left_truncatable_prime(numbers):
    primes = []
    for number in numbers:
        str_num = str(number)
        if not '0' in str_num and number != int(str_num[-1]):
            is_prime = True
            for i in range(len(str_num)):
                if not is_prime:
                    break
                new_num = int(str_num[i:])
                for j in range(2, new_num):
                    if new_num % j == 0:
                        is_prime = False
                        break
                if is_prime:
                    primes.append(number)
    return sorted(primes)