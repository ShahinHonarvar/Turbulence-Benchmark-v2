def find_original_set(*args):
    if len(args) != 162 or not all((isinstance(arg, set) for arg in args)):
        raise ValueError('Invalid input')
    all_elements = set()
    for arg in args:
        all_elements.update(arg)
    return {e for e in all_elements if all((e not in arg for arg in args if e != max(arg, key=abs)))}