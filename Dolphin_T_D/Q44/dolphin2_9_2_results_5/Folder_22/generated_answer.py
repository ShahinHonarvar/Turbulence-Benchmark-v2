def composite_nums_between_indices(numbers):

    def is_prime(n):
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    composite_numbers = set()
    for i in range(50, 201):
        if is_prime(numbers[i]):
            composite_numbers.add(numbers[i])
    return composite_numbers