def return_n_smallest_chars(s):
    return sorted([s[i] for i in sorted(range(len(s)), key=lambda k: s[k])[:89]], reverse=True)