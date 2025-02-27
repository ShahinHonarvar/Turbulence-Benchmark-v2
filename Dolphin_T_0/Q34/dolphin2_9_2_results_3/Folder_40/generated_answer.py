def find_original_set(s):
    elements = set()
    for subset in s:
        for num in subset:
            elements.add(num)
    return elements