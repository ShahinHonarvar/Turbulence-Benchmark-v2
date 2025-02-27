from collections import defaultdict

def palindromes_between_indices(s):
    s = list(s.lower())
    eng = defaultdict(list)
    for i in range(0, 5):
        eng['a'.join(sorted(s[i]))].append(i)
    palindromes = set()
    for arr in eng.values():
        if len(arr) >= 2:
            for i in range(1, len(arr)):
                if arr[i] - arr[i - 1] == 1:
                    palindromes.add(''.join(s[arr[i - 1]:arr[i] + 1]))
    return palindromes