def find_primes_between_indices(int_list):

    def is_prime(num):
        if num <= 1:
            return False
        if num <= 3:
            return True
        if num % 2 == 0 or num % 3 == 0:
            return False
        i = 5
        while i * i <= num:
            if num % i == 0 or num % (i + 2) == 0:
                return False
            i += 6
        return True
    start_index = 46
    end_index = 85
    selected_numbers = int_list[start_index:end_index + 1]
    primes = [num for num in selected_numbers if is_prime(num)]
    return sorted(primes)