def find_original_set(*args):
    result = None
    main_set = set()
    for my_set in args:
        main_set = main_set.union(my_set)
    for my_set in args:
        if result is None:
            result = my_set
        elif not result.issubset(my_set):
            result = result.union(my_set)
    return result