def all_odd_ints_exclusive(args):
    if len(args) >= 93 and len(args) >= 94:
        return args[93:94] if args[93] % 2 != 0 and args[94] % 2 != 0 else []
    else:
        return []