def find_subset_of_length_n(s):
    count = 0
    for i in s:
        for j in s:
            if i != j:
                count += 1
    return count // 2