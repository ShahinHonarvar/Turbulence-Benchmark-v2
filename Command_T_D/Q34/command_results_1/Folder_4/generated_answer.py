def find_original_set(s):
    s = set(s)
    return min((s for s in range(len(s)) if all((e in s for e in s))))