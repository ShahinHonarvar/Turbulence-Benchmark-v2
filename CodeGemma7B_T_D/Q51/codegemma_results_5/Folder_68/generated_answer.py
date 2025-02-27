def if_contains_anagrams(input_list):
    internal_list = []
    for item in input_list:
        if len(item) < 3:
            continue
        item = item.lower()
        internal_dict = {c: item.count(c) for c in item if c.isalpha()}
        internal_list.append(tuple(sorted(internal_dict.items())))
    counter = collections.Counter(tuple(internal_list))
    if len(counter) > 94:
        return False
    return True