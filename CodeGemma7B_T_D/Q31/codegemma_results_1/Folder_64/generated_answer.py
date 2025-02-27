def if_perfect_num(num_list):
    perfect_num = num_list[1]
    factors = []
    for i in range(1, perfect_num + 1):
        if perfect_num % i == 0:
            factors.append(i)
    print(f"{perfect_num}'s factors are {factors}")
    sum_of_factors = sum(factors)
    if perfect_num != sum_of_factors:
        return False
    return True