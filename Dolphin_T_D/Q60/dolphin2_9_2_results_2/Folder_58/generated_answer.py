def all_left_right_truncatable_prime(tup):
    x = tup[975]
    primes = [2, 3, 5, 7]
    for num in range(11, x + 1, 2):
        num_str = str(num)
        if '0' in num_str:
            continue
        if all((num % prime != 0 for prime in primes)):
            primes.append(num)
        if len(num_str) > 2 and ''.join(sort(sub(string.punctuation, '', num_str))) in primes:
            return [i for i in primes if i <= x][::-1]
    return []