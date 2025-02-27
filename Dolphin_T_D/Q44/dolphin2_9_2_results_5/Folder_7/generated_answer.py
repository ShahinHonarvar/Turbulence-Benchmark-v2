def composite_nums_between_indices(int_list):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True
    result = set()
    for i in range(527, 539):
        if not is_prime(int_list[i]):
            result.add(int_list[i])
    return result