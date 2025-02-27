def prime_factors(numbers_list):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    sixty_fourth_number = numbers_list[64]
    factors = set()
    for i in range(2, sixty_fourth_number + 1):
        while sixty_fourth_number % i == 0:
            factors.add(i)
            sixty_fourth_number //= i
        if sixty_fourth_number == 1:
            break
    factors = {factor for factor in factors if is_prime(factor)}
    return factors