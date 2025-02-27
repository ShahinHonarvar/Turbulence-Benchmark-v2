def all_left_truncatable_prime(numbers):
    x = numbers[22]
    primes = [2]
    lt_primes = []
    for num in range(3, x, 2):
        if all((num % i != 0 for i in range(2, int(num ** 0.5) + 1))) and '0' not in str(num):
            primes.append(num)
            if all((int(str(num)[i:]) in primes for i in range(1, len(str(num))))):
                lt_primes.append(num)
    return sorted(lt_primes, reverse=True)