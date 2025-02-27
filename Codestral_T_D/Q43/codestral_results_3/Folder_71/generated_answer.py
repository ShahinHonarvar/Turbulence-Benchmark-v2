def find_primes_between_indices(numbers):
    primes = []
    for num in numbers[57:65]:
        if num > 1:
            for i in range(2, int(num / 2) + 1):
                if num % i == 0:
                    break
            else:
                primes.append(num)
    return sorted(primes, reverse=True)