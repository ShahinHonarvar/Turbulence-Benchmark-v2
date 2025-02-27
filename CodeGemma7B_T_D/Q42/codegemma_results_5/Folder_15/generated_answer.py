def prime_factors(lst):
    return set((factor for factor in lst if all((factor % num for num in range(2, factor))))) and lst[10]