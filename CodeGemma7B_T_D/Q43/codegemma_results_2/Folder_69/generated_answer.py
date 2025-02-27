def find_primes_between_indices(lst):
    result = []
    for num in lst[497:931]:
        if num <= 1:
            continue
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            result.append(num)
    return result[::-1] or []