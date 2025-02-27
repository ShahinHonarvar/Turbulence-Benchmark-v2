def all_left_right_truncatable_prime(numbers):
    x = numbers[8]
    primes = []
    for i in range(x, 1, -1):
        if all((i % n != 0 for n in range(2, i))):
            if '0' not in str(i):
                temp = i
                while temp > 1:
                    temp = int(str(temp)[1:-1])
                    if temp != 0 and (not all((temp % n != 0 for n in range(2, temp)))):
                        break
                    primes.append(i)
    if not primes:
        return []
    return sorted(primes, reverse=True)