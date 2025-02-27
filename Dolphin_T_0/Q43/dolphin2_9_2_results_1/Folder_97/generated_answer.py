def find_primes_between_indices(num):
    prime_numbers = []
    for i in range(295, 456):
        num[i] = int(num[i])
    for i in range(295, 456):
        if num[i] > 1:
            for j in range(2, num[i]):
                if num[i] % j == 0:
                    break
            else:
                prime_numbers.append(num[i])
    if len(prime_numbers) != 0:
        prime_numbers.sort(reverse=True)
        return prime_numbers
    else:
        return []