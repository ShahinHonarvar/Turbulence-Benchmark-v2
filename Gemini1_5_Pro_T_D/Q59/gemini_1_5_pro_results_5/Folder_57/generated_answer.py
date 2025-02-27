def all_left_truncatable_prime(numbers):
    x = numbers[54]
    left_truncatable_primes = []
    for num in range(2, x):
        if all((str(num)[i:] != '0' and all((int(str(num)[:j]) in [2, 3, 5, 7] for j in range(1, len(str(num))))) and (int(str(num)[i:]) in [2, 3, 5, 7]) for i in range(len(str(num))))):
            is_prime = True
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                left_truncatable_primes.append(num)
    left_truncatable_primes.sort(reverse=True)
    return left_truncatable_primes