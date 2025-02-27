def all_left_right_truncatable_prime(numbers):
    primes = []
    x = numbers[43]
    for i in range(2, x + 1):
        if is_prime(i):
            in_list = True
            for j in range(1, len(str(i)) - 1):
                if '0' in str(i):
                    in_list = False
                    break
                if int(str(i)[j:]) not in primes:
                    in_list = False
                    break
                if int(str(i)[:-j - 1]) not in primes:
                    in_list = False
                    break
            if in_list:
                primes.append(i)
    primes.sort()
    return primes

def is_prime(n):
    if n <= 1 or (n % 2 == 0 and n > 2):
        return False
    return all((n % i for i in range(3, int(n ** 0.5) + 1, 2)))