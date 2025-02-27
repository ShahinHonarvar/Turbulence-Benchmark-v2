def find_subset_of_length_n(data):
    count = 0
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            for k in range(j + 1, len(data)):
                for l in range(k + 1, len(data)):
                    for m in range(l + 1, len(data)):
                        count += 1
    return count