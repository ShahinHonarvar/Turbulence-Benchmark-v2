def find_primes_between_indices(lst):
    primes = []
    for i in range(80, 85):
        if i < len(lst):
            numbers = lst[i]
            for num in range(2, numbers + 1):
                if all((num % i != 0 for i in range(2, num))):
                    primes.append(numbers)
                    break
    return sorted(primes, reverse=True)