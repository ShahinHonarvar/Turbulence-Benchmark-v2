def find_original_set(*args):
    all_elements = {}
    for s in args:
        for i in s:
            if i not in all_elements:
                all_elements[i] = 1
    original_set = set()
    for key, value in all_elements.items():
        original_set.add(key)
    return original_set