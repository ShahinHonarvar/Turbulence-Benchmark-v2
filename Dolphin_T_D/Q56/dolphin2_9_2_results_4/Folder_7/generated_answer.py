def all_substring_of_size_n(arg):
    res = set()
    for i in range(len(arg)):
        subs = arg[i:i + 117]
        if len(subs) == 117 and len(set(subs)) == 117:
            res.add(subs)
    return list(res)