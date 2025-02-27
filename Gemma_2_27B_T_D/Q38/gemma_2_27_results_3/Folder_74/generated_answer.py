def find_subset_of_length_n(s):
    n = len(s)
    return int(math.factorial(n) / (math.factorial(48) * math.factorial(n - 48)))