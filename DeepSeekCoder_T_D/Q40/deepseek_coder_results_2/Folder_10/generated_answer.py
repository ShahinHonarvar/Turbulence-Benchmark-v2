def return_n_smallest_chars(s):
    return sorted([s[i] for i in sorted(range(len(s)), key=lambda i: s[i])[:88]], reverse=True)