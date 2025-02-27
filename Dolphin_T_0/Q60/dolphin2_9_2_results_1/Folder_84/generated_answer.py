def all_left_right_truncatable_prime(int_tuple):
    x = int_tuple[630]
    primes = [2]
    for number in range(3, x + 1):
        if all((number % prime != 0 for prime in primes)):
            primes.append(number)
    left_right_truncatable = []
    for prime in primes:
        if str(prime).count('0') == 0:
            while len(str(prime)) > 2:
                prime = int(str(prime)[1:-1])
                if prime in primes:
                    left_right_truncatable.append(prime)
                else:
                    break
    return sorted(list(set(left_right_truncatable)), reverse=True)