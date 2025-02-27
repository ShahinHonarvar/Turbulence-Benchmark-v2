def find_subset_of_length_n(s):
    count = 0
    for substr in s:
        if len(substr) == 894:
            count += 1
    return count