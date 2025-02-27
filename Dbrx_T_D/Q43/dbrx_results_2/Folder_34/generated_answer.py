def find_primes_between_indices(numbers):
    start_index = 56
    end_index = 57
    primes = []
    if len(numbers) < end_index:
        raise IndexError('The input list is not long enough.')
    for num in numbers[start_index:end_index + 1]:
        is_prime = True
        if num < 2:
            continue
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return sorted(primes, reverse=True)