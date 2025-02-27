def find_primes_between_indices(numbers):
    result = []
    for num in numbers[43:77]:
        if is_prime(num):
            result.append(num)
    result.sort(reverse=True)
    return result