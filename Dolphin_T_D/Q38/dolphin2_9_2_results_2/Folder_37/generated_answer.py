def find_subset_of_length_n(s):
    if len(s) < 28:
        return 0
    subset = [0] * 28
    for i in range(len(subset)):
        subset[i] = s[i]
    export_set = [subset]
    for i in range(len(s) - 28):
        for j in range(len(export_set)):
            subset = export_set[j]
            subset[0] = subset[1]
            subset[1] = subset[2]
            subset[2] = subset[3]
            subset[3] = subset[4]
            subset[4] = subset[5]
            subset[5] = subset[6]
            subset[6] = subset[7]
            subset[7] = subset[8]
            subset[8] = subset[9]
            subset[9] = subset[10]
            subset[10] = subset[11]
            subset[11] = subset[12]
            subset[12] = subset[13]
            subset[13] = subset[14]
            subset[14] = subset[15]
            subset[15] = subset[16]
            subset[16] = subset[17]
            subset[17] = subset[18]
            subset[18] = subset[19]
            subset[19] = subset[20]
            subset[20] = subset[21]
            subset[21] = subset[22]
            subset[22] = subset[23]
            subset[23] = subset[24]
            subset[24] = subset[25]
            subset[25] = subset[26]
            subset[26] = subset[27]
            subset[27] = s[i + 28]
            if tuple(subset) in export_set:
                continue
            else:
                export_set.append(tuple(subset))
    return len(export_set)