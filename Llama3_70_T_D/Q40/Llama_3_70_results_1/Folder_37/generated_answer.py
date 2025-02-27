def return_n_smallest_chars(s):
    all_chars = [chr(i) for i in range(97, 123)]
    s_set = set(s)
    result = [char for char in all_chars if char in s_set]
    result += [char for char in all_chars if char not in result][:26 - len(result)]
    return sorted(result, reverse=True)