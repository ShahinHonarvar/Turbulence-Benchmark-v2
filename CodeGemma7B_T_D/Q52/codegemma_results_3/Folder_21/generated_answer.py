from collections import defaultdict

def find_permutations(prefix, suffix, path=[], permutation=[]):
    if len(path) == len(prefix) + len(suffix):
        yield permutation.copy()
        return
    if path:
        permutation.append(path[-1])
        yield from find_permutations(prefix, suffix, path, permutation)
        permutation.pop()
    if prefix:
        for i in range(len(prefix)):
            path.append(prefix[i])
            yield from find_permutations(prefix[i + 1:], suffix, path, permutation)
            path.pop()
    if suffix:
        for i in range(len(suffix)):
            path.append(suffix[i])
            yield from find_permutations(prefix, suffix[i + 1:], path, permutation)
            path.pop()