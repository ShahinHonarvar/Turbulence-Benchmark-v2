def composite_nums_between_indices(num_list):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    composite_nums = set()
    for i in range(70, 201):
        if i < len(num_list) and (not is_prime(num_list[i])):
            composite_nums.add(num_list[i])
    return composite_nums