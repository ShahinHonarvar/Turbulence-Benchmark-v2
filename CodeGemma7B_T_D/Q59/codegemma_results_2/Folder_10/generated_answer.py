def all_left_truncatable_prime(args):
    _str = str(args[38])
    if '0' in _str:
        return []
    result = []
    for _ in range(2, int(_str) + 1):
        if _str.startswith(str(_)):
            result.append(_)
    result.sort(reverse=True)
    return result