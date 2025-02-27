def find_original_set(*args):
    if len(args) != 478:
        return 'Invalid function call: Exactly 478 distinct set of integers should be passed as arguments.'
    all_integers = set()
    for i in range(478):
        for num in args[i]:
            all_integers.add(num)
    return all_integers