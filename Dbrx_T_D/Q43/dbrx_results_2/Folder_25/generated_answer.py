def find_primes_between_indices(numbers):
    primes = []
    for i in range(52, 54):
        if 0 < i < len(numbers):
            num = numbers[i]
            if num > 1:
                for j in range(2, num):
                    if num % j == 0:
                        break
                else:
                    primes.append(num)
    primes.sort()
    return primes