def all_left_truncatable_prime(tup):
    num = tuple(tup[370:])
    for i in [num, int(''.join(reversed(num)))]:
        if not any((str(i).endswith(str(j)) for j in num)) and all((str(i).startswith(str(j)) and isprime(int(j)) for j in num)):
            list_of_prime = sorted([int(k) for k in str(i)], reverse=True)
            return list_of_prime
        num = str(num)[1:]