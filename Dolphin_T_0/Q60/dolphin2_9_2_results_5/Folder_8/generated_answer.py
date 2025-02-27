def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = numbers[41]
    result = []
    for i in range(x, 0, -1):
        if is_prime(i) and (not '0' in str(i)):
            string_i = str(i)
            while len(string_i) > 1:
                if not is_prime(int(string_i[1:-1])):
                    break
                string_i = string_i[1:-1]
            else:
                result.append(i)
    return sorted(result, reverse=True)