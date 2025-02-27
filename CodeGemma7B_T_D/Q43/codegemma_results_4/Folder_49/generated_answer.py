def find_primes_between_indices(int_list):
    result = []
    for i in range(22, 51):
        if int_list[i] <= 1:
            continue
        for j in range(2, int(int_list[i] / 2) + 1):
            if int_list[i] % j == 0:
                break
        else:
            result.append(int_list[i])
    return sorted(result, reverse=True)