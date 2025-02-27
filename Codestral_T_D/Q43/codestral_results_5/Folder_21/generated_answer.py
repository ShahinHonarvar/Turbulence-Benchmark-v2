def find_primes_between_indices(numbers):
    start = max(478, 0)
    end = min(949, len(numbers) - 1)
    primes = []
    for i in range(start, end + 1):
        num = numbers[i]
        if num > 1:
            for j in range(2, int(num ** 0.5) + 1):
                if num % j == 0:
                    break
            else:
                primes.append(num)
    return sorted(primes, reverse=True)