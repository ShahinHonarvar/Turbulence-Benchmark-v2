def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[92]
    primes = []
    for i in range(2, x + 1):
        if '0' not in str(i) and len(str(i)) > 2:
            trunc = i
            while len(str(trunc)) > 1:
                trunc = int(str(trunc)[-1] + str(trunc)[1:-1] + str(trunc)[0])
                if not is_prime(trunc):
                    break
            if len(str(trunc)) == 2 and is_prime(trunc):
                primes.append(i)
    return sorted(primes)