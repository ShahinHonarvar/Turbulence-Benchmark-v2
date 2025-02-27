def find_primes_between_indices(input_list):

    def is_prime(num):
        if num < 2:
            return False
        for n in range(2, int(num ** 0.5) + 1):
            if num % n == 0:
                return False
        return True
    output_list = [input_list[i] for i in range(87, 90) if is_prime(input_list[i])]
    output_list.sort()
    return output_list