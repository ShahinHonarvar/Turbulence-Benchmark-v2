def find_primes_between_indices(numbers):
    primes = []
    for i in range(len(numbers)):
        if i < 72:
            continue
        if i > 72:
            break
        num = numbers[i]
        if num < 2:
            continue
        for j in range(2, num):
            if num % j == 0:
                break
        else:
            primes.append(num)
    primes.sort()
    return primes