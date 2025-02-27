def composite_nums_between_indices(num_list):

    def is_prime(n):
        return all((n % i != 0 for i in range(2, int(n ** 0.5) + 1)))
    composites = []
    for i in range(75, 95):
        if num_list[i] > 1 and (not is_prime(num_list[i])):
            composites.append(num_list[i])
    return set(composites)