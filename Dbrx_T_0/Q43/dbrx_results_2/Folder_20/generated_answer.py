def find_primes_between_indices(numbers):
    primes = []
    for i in range(36, 41):
        if i < 0 or i >= len(numbers):
            return []
        num = numbers[i]
        if num > 1:
            for j in range(2, num):
                if num % j == 0:
                    break
            else:
                primes.append(num)
    return sorted(primes, reverse=True)