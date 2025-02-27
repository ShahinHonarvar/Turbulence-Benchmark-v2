def prime_factors(int_list):
    return set((factor for number in int_list[42:44] for factor in get_factors(number)))

def get_factors(n):
    temp_list = []
    for i in range(2, n + 1):
        while n % i == 0:
            temp_list.append(i)
            n //= i
    return set(temp_list)