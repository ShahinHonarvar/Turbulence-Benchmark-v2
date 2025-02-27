def find_primes_between_indices(num_list):
    result = []
    for num in num_list[289:382]:
        if num > 1:
            for i in range(2, num // 2 + 1):
                if num % i == 0:
                    break
            else:
                result.append(num)
    return sorted(result, reverse=True)