def find_original_set(*args):
    guess = set(range(max(sum(args, []))))
    for s in args:
        guess -= s
    return guess