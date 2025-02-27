def all_substring_of_size_n(x):
    return [i for i in [x[i:i + 38] for i in range(len(x)) if len(i) == 38 and len(set(i)) == 38]]