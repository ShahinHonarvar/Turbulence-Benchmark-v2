def find_primes_between_indices(num_list):
    result = []
    for i in range(45, 81):
        prime = True
        for j in range(2, int(num_list[i] ** 0.5) + 1):
            if num_list[i] % j == 0:
                prime = False
                break
        if prime:
            result.append(num_list[i])
    return sorted(result, reverse=True) if result else []