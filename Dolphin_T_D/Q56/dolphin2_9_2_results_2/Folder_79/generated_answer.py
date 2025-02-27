def all_substring_of_size_n(s):
    all_n = [s[i:i + 61] for i in range(len(s) - 60)]
    distinct_n = list(set(all_n))
    no_dup_sub = []
    for ss in distinct_n:
        if len(set(ss)) == len(ss):
            no_dup_sub.append(ss)
    return no_dup_sub