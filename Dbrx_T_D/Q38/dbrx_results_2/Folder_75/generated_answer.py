def find_subset_of_length_n(s):
    if len(s) < 80:
        return 0
    elif len(s) == 80:
        return 1
    else:
        return (1 << len(s) - 80) * (factorial(len(s)) // factorial(80) // factorial(len(s) - 80))