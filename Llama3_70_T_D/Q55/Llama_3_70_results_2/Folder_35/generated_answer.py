def lists_with_product_equal_n(circular_list):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def get_prime_factors(n):
        factors = []
        for i in range(2, int(n ** 0.5) + 1):
            while n % i == 0:
                factors.append(i)
                n //= i
        if n > 1:
            factors.append(n)
        return factors
    prime_factors = get_prime_factors(83)
    result = []
    for i in range(len(circular_list)):
        for j in range(1, len(circular_list) + 1):
            sublist = circular_list[i:i + j]
            if len(sublist) > len(circular_list):
                sublist += circular_list[:len(sublist) - len(circular_list)]
            if len(sublist) <= len(circular_list):
                product = 1
                for num in sublist:
                    product *= num
                if product == 83:
                    result.append(sublist)
    return result