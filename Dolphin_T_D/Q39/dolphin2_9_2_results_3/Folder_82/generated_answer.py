def return_n_greatest_chars(s):
    return sorted(([x for x in s if x not in ' '] for x in range(60)))